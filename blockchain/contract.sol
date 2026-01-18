// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AllocationAudit {
    event AllocationLogged(uint allocationId);

    function logAllocation(uint allocationId) public {
        emit AllocationLogged(allocationId);
    }
}
