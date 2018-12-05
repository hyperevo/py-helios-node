from typing import (
    Tuple,
    Dict,
    Any,
)

from cytoolz import (
    compose,
)

from helios.protocol.common.datastructures import ChronologicalBlockHashFragmentBundle
from hvm.db.trie import make_trie_root_and_nodes
from eth_hash.auto import keccak
import rlp

from helios.protocol.common.normalizers import (
    BaseNormalizer,
)
from helios.protocol.common.types import (
    BlockBodyBundles,
    NodeDataBundles,
    ReceiptsBundles,
    ReceiptsByBlock,
)
from helios.rlp_templates.hls import BlockBody
from hvm.rlp.consensus import NodeStakingScore


class GetNodeDataNormalizer(BaseNormalizer[Tuple[bytes, ...], NodeDataBundles]):
    is_normalization_slow = True

    @staticmethod
    def normalize_result(msg: Tuple[bytes, ...]) -> NodeDataBundles:
        node_keys = tuple(map(keccak, msg))
        result = tuple(zip(node_keys, msg))
        return result


class ReceiptsNormalizer(BaseNormalizer[ReceiptsByBlock, ReceiptsBundles]):
    is_normalization_slow = True

    @staticmethod
    def normalize_result(message: ReceiptsByBlock) -> ReceiptsBundles:
        trie_roots_and_data = tuple(map(make_trie_root_and_nodes, message))
        return tuple(zip(message, trie_roots_and_data))


class GetBlockBodiesNormalizer(BaseNormalizer[Tuple[BlockBody, ...], BlockBodyBundles]):
    is_normalization_slow = True

    @staticmethod
    def normalize_result(msg: Tuple[BlockBody, ...]) -> BlockBodyBundles:
        uncles_hashes = tuple(map(
            compose(keccak, rlp.encode),
            tuple(body.uncles for body in msg)
        ))
        transaction_roots_and_trie_data = tuple(map(
            make_trie_root_and_nodes,
            tuple(body.transactions for body in msg)
        ))

        body_bundles = tuple(zip(msg, transaction_roots_and_trie_data, uncles_hashes))
        return body_bundles


class GetNodeStakingScoreNormalizer(BaseNormalizer[Dict[str, NodeStakingScore], NodeStakingScore]):
    is_normalization_slow = False

    @staticmethod
    def normalize_result(msg: Dict[str, NodeStakingScore]) -> NodeStakingScore:
        result = msg['node_staking_score']
        return result


class GetChronoligcalBlockHashFragmentsNormalizer(BaseNormalizer[Dict[str, Any], ChronologicalBlockHashFragmentBundle]):
    is_normalization_slow = False

    @staticmethod
    def normalize_result(msg: Dict[str, Any]) -> ChronologicalBlockHashFragmentBundle:
        result = ChronologicalBlockHashFragmentBundle(fragments = msg['fragments'],
                                                      root_hash_of_just_this_chronological_block_window = msg['root_hash_of_just_this_chronological_block_window'])
        return result

