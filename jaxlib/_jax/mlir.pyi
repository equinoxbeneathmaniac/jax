# Copyright 2021 The JAX Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from . import XlaComputation

def hlo_to_stablehlo(computation: bytes) -> bytes: ...
def xla_computation_to_mlir_module(computation: XlaComputation) -> str: ...
def mlir_module_to_xla_computation(
    mlir_module: bytes | str,
    use_tuple_args: bool = ...,
    return_tuple: bool = ...,
) -> XlaComputation: ...
def mhlo_to_stablehlo(mlir_module: bytes | str) -> bytes: ...
def stablehlo_to_mhlo(mlir_module: bytes | str) -> bytes: ...
def serialize_portable_artifact(mlir_module: str, target: str, use_mixed_serialization: bool = True) -> bytes: ...
def deserialize_portable_artifact(mlir_module: bytes) -> str: ...
def refine_polymorphic_shapes(
    mlir_module: bytes | str,
    enable_shape_assertions: bool = ...,
    validate_static_shapes: bool = ...,
    enable_shardy: bool = ...,
) -> bytes: ...
