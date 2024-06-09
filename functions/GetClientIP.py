from flask import Request

class GetClientIP:

    @staticmethod
    def get_client_ip(request: Request) -> str:
        if request.environ.get('HTTP_X_FORWARDED_FOR'):
            ip = request.environ['HTTP_X_FORWARDED_FOR']
        elif request.environ.get('HTTP_X_REAL_IP'):
            ip = request.environ['HTTP_X_REAL_IP']
        else:
            ip = request.remote_addr
        return ip