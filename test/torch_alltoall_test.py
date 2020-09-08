#
# Copyright (C) Mellanox Technologies Ltd. 2001-2020.  ALL RIGHTS RESERVED.
#

from torch_ucc_test_setup import *

args = parse_test_args()
pg = init_process_groups(args.backend)

comm_size = dist.get_world_size()
comm_rank = dist.get_rank()

counts = [comm_size]
for i in range(20):
    counts.append(counts[-1] * 2)

print_test_head("Alltoall", comm_rank)
for count in counts:
    send_tensor = get_tensor(count, args.use_cuda)
    recv_tensor_ucc = get_tensor(count, args.use_cuda)
    recv_tensor_test = get_tensor(count, args.use_cuda)
    dist.all_to_all_single(recv_tensor_ucc, send_tensor)
    dist.all_to_all_single(recv_tensor_test, send_tensor, group=pg)
#    print("rank {}: input {} ucc {} mpi {}".format(comm_rank, send_tensor, recv_tensor_ucc, recv_tensor_test))
    status = check_tensor_equal(recv_tensor_ucc, recv_tensor_test)
    dist.all_reduce(status, group=pg)
    print_test_result(status, count, comm_rank, comm_size)

if comm_rank == 0:
    print("Test alltoall: succeeded")
