import logging


class IncompleteFeatureException(Exception):
    ...


def grpc_getter_cmd(stub, proto_lib, fn_name: str, query_args=None):
    fn = getattr(stub, fn_name)
    feature = fn(query_args or proto_lib.google_dot_protobuf_dot_empty__pb2.Empty())
    if not feature:
        raise IncompleteFeatureException()
    logging.debug(f"Feature called {feature}")
    return feature


def grpc_setter_cmd(stub, proto_lib, fn_name: str, class_name: str, **kwargs) -> None:
    fn = getattr(stub, fn_name)
    c = getattr(proto_lib, class_name)
    fn(c(**kwargs))
