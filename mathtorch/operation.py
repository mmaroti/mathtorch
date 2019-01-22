#!/usr/bin/env python
#
# Copyright (C) 2019, Miklos Maroti
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import torch


class Operation(object):
    """Represents an n-ary operation on a k-element set using an n+1 rank
    [k,k,...,k] shaped real tensor from input dimensions to the result."""

    def __init__(self, tensor):
        self.tensor = tensor
        self.arity = len(tensor.shape) - 1
        assert self.arity >= 0
        self.domain = tensor.shape[0]
        for i in range(1, len(tensor.shape)):
            assert self.domain == tensor.shape[i]

    def apply(self, args):
        """The arguments must be an arity sized array of broadcastable tensors. 
        The last dimension of the argument represent the elements and they
        must be of domain size."""

        assert len(args) == self.arity

        args2 = list(args)
        for i in range(self.arity):
            assert args2[i].shape[-1] == self.domain
            for j in range(self.arity):
                if j < i:
                    args2[i] = args2[i].unsqueeze(-2)
                elif j > i:
                    args2[i] = args2[i].unsqueeze(-1)
            print(args2[i].shape)


class AdditionOp(Operation):
    """The binary modulo addition operation on a finite domain."""

    def __init__(self, domain):
        assert domain >= 1
        tensor = torch.empty([domain, domain, domain], dtype=torch.float32)
        for i in range(domain):
            for j in range(domain):
                for k in range(domain):
                    tensor[i, j, k] = 1.0 if (i + j) % domain == k else 0.0

        super(AdditionOp, self).__init__(tensor)
        assert self.domain == domain and self.arity == 2


if __name__ == "__main__":
    op = AdditionOp(3)
    a = torch.tensor([1, 0, 0])
    op.apply([a, a])
