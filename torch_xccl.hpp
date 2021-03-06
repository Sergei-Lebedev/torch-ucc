/**
 * * Copyright (C) Mellanox Technologies Ltd. 2001-2020.  ALL RIGHTS RESERVED.
 * *
 * * See file LICENSE for terms.
 * */

#pragma once

#include <api/xccl.h>
#include "torch_ucc_sendrecv.hpp"

namespace c10d {

struct torch_xccl_comm_t {
    torch_ucx_comm_t *p2p_comm;
    xccl_lib_h       xccl_lib;
    xccl_context_h   xccl_ctx;
    xccl_team_h      xccl_team;
};

torch_ucx_status_t torch_xccl_comm_init(torch_ucx_comm_t *p2p_comm,
                                        torch_xccl_comm_t **comm);

void torch_xccl_comm_close(torch_xccl_comm_t *comm);

}
