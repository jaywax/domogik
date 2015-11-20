from domogik.admin.application import app, json_response, timeit
import sys
import os
import domogik
import json
from subprocess import Popen, PIPE
from flask import Response, request
from domogikmq.message import MQMessage
from domogikmq.reqrep.client import MQSyncReq
import traceback

@app.route('/rest/butler/discuss', methods=['POST'])
@json_response
@timeit
def api_butler_discuss():
    """
    @api {post} /butler/discuss Discuss with the butler
    @apiName postButlerDiscuss
    @apiGroup Butler
    @apiVersion 0.5.0

    @apiParam {Number} id The commandId to generate
    @apiParam Key A key value pair for each command param

    @apiExample Example usage with wget
        $ wget -qO- http://192.168.1.10:40405/butler/discuss --post-data='{"text" : "hello", "source" : "a_script"}' --header="Content-type: application/json"
        {
            "identity": "Aria", 
            "location": null, 
            "media": null, 
            "mood": null, 
            "reply_to": "a_script", 
            "sex": "female", 
            "text": "hi"
        }

    @apiSuccessExample Success-Response:
        HTTTP/1.1 200 
        {
            "identity": "Aria", 
            "location": null, 
            "media": null, 
            "mood": null, 
            "reply_to": "a_script", 
            "sex": "female", 
            "text": "hi"
        }

    @apiErrorExample Butler does not respond in time
        HTTTP/1.1 400 Bad Request
        {
            msg: "butler does not respond"
        }
    
    @apiErrorExample Other error
        HTTTP/1.1 400 Bad Request
        {
            msg: "error while parsing butler response : ...'
        }
    """
    try:
        json_data = json.loads(request.data)
    except:
        return 400, {'msg': u"Error while decoding received json data. Error is : {0}".format(traceback.format_exc())}

    cli = MQSyncReq(app.zmq_context)

    msg = MQMessage()
    msg.set_action('butler.discuss.do')
    msg.set_data(json_data)

    # do the request
    # we allow a long timeout because the butler can take some time to respond...
    # some functions are quite long (requests to external webservices, ...)
    resp = cli.request('butler', msg.get(), timeout=60)
    if resp:
        try:
            response = resp.get_data()
            return 200, response
        except:
            return 400, {'msg': u"error while parsing butler response : {0}".format(resp) }
    else:
        return 400, {'msg': "butler does not respond"}