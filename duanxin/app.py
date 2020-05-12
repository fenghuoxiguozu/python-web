import flask, json
from flask import request
import io

server = flask.Flask(__name__)
glob_msg=None

@server.route('/test', methods=['get', 'post'])
def test():
    return 'hello'

@server.route('/msg', methods=['get', 'post'])
def msg():
    if request.method == "POST":
        msg = request.form.get('msg')
        global glob_msg
        glob_msg=msg
        if msg:
            result = {'code': 200, 'message': '成功',"msg":msg}
            return json.dumps(result, ensure_ascii=False)
        else:
            return  json.dumps({'code': 400, 'message': '失败',"msg":msg}, ensure_ascii=False)
    if request.method == "GET":
        return json.dumps({"msg":glob_msg},ensure_ascii=False)

if __name__ == '__main__':
    server.run(debug=True,host='192.168.1.3',port=5000)
