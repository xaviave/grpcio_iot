# grpcio_iot
gRPC io based helper to simplify python development with gRPC

## Definition

- `grpc_getter_cmd`  
	The function will handle the query_args or provide am empty `google_dot_protobuf_dot_empty__pb2.Empty()`.
	Args:
	* server `stub`
    * `proto_lib` import
    * `ProtoBuf` defined function name

	The ProtoBuf function's result is returned 

- `grpc_setter_cmd`
	The function will set a class from the given arguments.	

	Args:
    * server `stub`
    * `proto_lib` import
    * `ProtoBuf` defined function name
    * `ProtoBuf` defined class name
    * `kwargs`: arguments use to create the `ProtoBuf` class. 
