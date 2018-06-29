class PyEVMError(Exception):
    """
    Base class for all py-evm errors.
    """
    pass


class VMNotFound(PyEVMError):
    """
    Raised when no VM is available for the provided block number.
    """
    pass


class StateRootNotFound(PyEVMError):
    """
    Raised when the requested state root is not present in our DB.
    """
    pass


class HeaderNotFound(PyEVMError):
    """
    Raised when a header with the given number/hash does not exist.
    """
    

class BlockNotFound(PyEVMError):
    """
    Raised when the block with the given number/hash does not exist.
    """
    pass

class BlockOnWrongChain(PyEVMError):
    """
    Raised when a block interacts with a chain it doesnt belong to
    """
    pass


class IncorrectBlockType(PyEVMError):
    """
    Raised when the block is queueblock when it should be block or vice-versa
    """
    pass

class IncorrectBlockHeaderType(PyEVMError):
    """
    Raised when the block is queueblock when it should be block or vice-versa
    """
    pass

class NotEnoughTimeBetweenBlocks(PyEVMError):
    """
    Raised when there is not enough time between blocks. WHO WOULD HAVE GUESSED?
    """
    pass

class CannotCalculateStake(PyEVMError):
    """
    Raised when a function tries to calculate the stake for an address where we are missing information. for example, if we dont have their chain.
    """
    pass


class TransactionNotFound(PyEVMError):
    """
    Raised when the transaction with the given hash or block index does not exist.
    """
    pass

class InvalidHeadRootTimestamp(PyEVMError):
    """
    Raised when a timestamp based head hash is loaded or saved with invalid timestamp
    """
    pass

class ParentNotFound(HeaderNotFound):
    """
    Raised when the parent of a given block does not exist.
    """
    pass


class CanonicalHeadNotFound(PyEVMError):
    """
    Raised when the chain has no canonical head.
    """
    pass


class CollationHeaderNotFound(PyEVMError):
    """
    Raised when the collation header for the given shard and period does not exist in the database.
    """
    pass


class CollationBodyNotFound(PyEVMError):
    """
    Raised when the collation body for the given shard and period does not exist in the database.
    """
    pass


class CanonicalCollationNotFound(PyEVMError):
    """
    Raised when no collation for the given shard and period has been marked as canonical.
    """
    pass


class ValidationError(PyEVMError):
    """
    Raised when something does not pass a validation check.
    """
    pass


class Halt(PyEVMError):
    """
    Raised when an opcode function halts vm execution.
    """
    pass


class VMError(PyEVMError):
    """
    Base class for errors raised during VM execution.
    """
    burns_gas = True
    erases_return_data = True


class OutOfGas(VMError):
    """
    Raised when a VM execution has run out of gas.
    """
    pass


class InsufficientStack(VMError):
    """
    Raised when the stack is empty.
    """
    pass


class FullStack(VMError):
    """
    Raised when the stack is full.
    """
    pass


class InvalidJumpDestination(VMError):
    """
    Raised when the jump destination for a JUMPDEST operation is invalid.
    """
    pass


class InvalidInstruction(VMError):
    """
    Raised when an opcode is invalid.
    """
    pass


class InsufficientFunds(VMError):
    """
    Raised when an account has insufficient funds to transfer the
    requested value.
    """
    pass

class ReceiveTransactionIncorrectSenderBlockHash(VMError):
    """
    Raised when a receive transaction is found that has a sender block hash
    that doesnt match the one in our database.
    """
    pass

class ReceiveTransactionNotInDb(VMError):
    """
    Raised when a receive transaction is not found in our db
    """
    pass

class ReceivingTransactionForWrongWallet(VMError):
    """
    Raised when a someone tries to receive a transaction sent to someone else.
    """
    pass




class StackDepthLimit(VMError):
    """
    Raised when the call stack has exceeded it's maximum allowed depth.
    """
    pass


class ContractCreationCollision(VMError):
    """
    Raised when there was an address collision during contract creation.
    """
    pass


class IncorrectContractCreationAddress(VMError):
    """
    Raised when the address provided by transaction does not
    match the calculated contract creation address.
    """
    pass


class Revert(VMError):
    """
    Raised when the REVERT opcode occured
    """
    burns_gas = False
    erases_return_data = False


class WriteProtection(VMError):
    """
    Raised when an attempt to modify the state database is made while
    operating inside of a STATICCALL context.
    """
    pass


class OutOfBoundsRead(VMError):
    """
    Raised when an attempt was made to read data beyond the
    boundaries of the buffer (such as with RETURNDATACOPY)
    """
    pass
