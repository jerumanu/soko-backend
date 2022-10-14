
# 200 OK - [GET]: The server successfully returned the data requested by the user
# 201 CREATED - [POST/PUT/PATCH]: User created or modified data successfully
# 202 Accepted - [*]: Indicates that a request has entered the background queue (asynchronous task)
# 204 NO CONTENT - [DELETE]: User successfully deleted data
# 400 INVALID REQUEST - [POST/PUT/PATCH]: There is an error in the request sent by the user, and the server does not create or modify data
# 401 Unauthorized - [*]: Indicates that the user is not authorized (token, username, password error)
# 403 Forbidden - [*] means the user is authorized (as opposed to a 401 error), but access is forbidden
# 404 NOT FOUND - [*]: The request sent by the user is for a record that does not exist, and the server does not operate
# 406 Not Acceptable - [GET]: The format requested by the user is not available
# 410 Gone -[GET]: The resource requested by the user is permanently deleted and will not be available again
# 422 Unprocesable entity - [POST/PUT/PATCH] A validation error occurred when creating an object
# 500 INTERNAL SERVER ERROR - [*]: An error has occurred on the server, and the user will not be able to determine whether the sent request is successful or not
from flask import make_response,jsonify
# from  . import blueprint
from app.main.auth.extensions.auth.jwt_auth import auth

error_list = {
    # success status code
    0: "success",

    # User error:
    #20000: "Account activated successfully",
    20001: "User does not exist",
    20002: "Account has been disabled",
    20003: "Invalid password",
    20004: "User already exists",
    20005: "User is not logged in",
    20006: "The email address is invalid, please use a valid email address",
    20007: "Username and password cannot be empty",
    20008: "Account not activated, please check email",
    20009: "User activation failed, token invalid or incorrect email address, please contact the administrator.",

    # User succeeded:
    30000: "Login successful",
    30001: "Account registration is successful, please click the activation link to activate the account.",
    30002: "Account has been activated successfully",

    # Parameter error:
    10001: "Parameter is empty",
    10002: "Invalid parameter",
    10003: "Incorrect parameter type",
    10004: "parameter missing",
}


# Parameter error: 10001-19999 */
PARAM_IS_INVALID = ({"message": "Invalid parameter", "return_code": 10001 })
PARAM_IS_BLANK = ({"message": "parameter is empty", "return_code": 10002 })
PARAM_TYPE_BIND_ERROR = ({"message": "Parameter type error", "return_code": 10003 })
PARAM_NOT_COMPLETE = ({"message": "parameter missing", "return_code": 10004 })

# User error: 20001-29999 */
USER_NOT_LOGGED_IN = ({"message": "User is not logged in", "return_code": 20001 })
USER_LOGIN_ERROR = ({"message": "The account does not exist or the password is incorrect", "return_code": 20002,})
USER_ACCOUNT_FORBIDDEN = ({"message": "Account has been disabled", "return_code":20003})
USER_NOT_EXIST = ({"message": "User does not exist xxxxxxxxxxx", "return_code": 20004 })
USER_HAS_EXISTED = ({"message": "User already exists", "return_code": 20005})

# Business error: 30001-39999
#SPECIFIED_QUESTIONED_USER_NOT_EXIST(30001, "There is a problem with a business"})

# # System error: 40001-49999 */
# SYSTEM_INNER_ERROR(40001, "The system is busy, please try again later"),

# # Data error: 50001-599999 */
# RESULE_DATA_NONE(50001, "Data not found"),
# DATA_IS_WRONG(50002, "Data error"),
# DATA_ALREADY_EXISTED(50003, "Data already exists"),

# # Interface error: 60001-69999 */
# INTERFACE_INNER_INVOKE_ERROR(60001, "Internal system interface call exception"),
# INTERFACE_OUTTER_INVOKE_ERROR(60002, "External system interface call exception"),
# INTERFACE_FORBID_VISIT(60003, "Access to this interface is forbidden"),
# INTERFACE_ADDRESS_INVALID(60004, "The interface address is invalid"),
# INTERFACE_REQUEST_TIMEOUT(60005, "Interface request timeout"),
# INTERFACE_EXCEED_LOAD(60006, "Interface load too high"),

# # Permission error: 70001-79999 */
# PERMIS


SERVER_ERROR_500 = ({"message": "An error occured."}, 500)
NOT_FOUND_404 = ({"message": "Resource could not be found."}, 404)
NO_INPUT_400 = ({"message": "No input data provided."}, 400)
INVALID_INPUT_422 = ({"status":1,"message": "Invalid input."}, 422)

PASSWORD_INVALID_421 = ({"message": "Invalid password."}, 421)
ALREADY_EXIST = ({"status":1,"message": "Already exists."}, 409)

DOES_NOT_EXIST = ({"message": "Does not exists."}, 409)
NOT_ADMIN = ({"message": "Admin permission denied."}, 998)
HEADER_NOT_FOUND = ({"message": "Header does not exists."}, 999)

# custom error message
@auth.error_handler

def unauthorized():
    return make_response(jsonify(
        {   'status': 403,
            'message': 'unauthorized access'
        }), 403)



class CustomFlaskErr(Exception):
    status_code = 400
    def __init__(self,status_code=None,return_code=None,action_status=None,playbook=None):
        super().__init__(self)
        self.return_code = return_code
        self.status_code = status_code
        self.action_status = action_status
        self.playbook = playbook
       
    def to_dict(self):
        rv = dict()
        if self.playbook != None:
            rv['data'] = self.playbook
        else:
            print (self.playbook)
        rv['action_status'] = self.action_status
        rv['message'] = error_list.get(self.return_code)
        rv['return_code'] = self.return_code
        rv['status_code'] = self.status_code
        print(rv)
        return rv

# @blueprint.app_errorhandler(CustomFlaskErr)
def handle_flask_error(error):
    # response The json content is custom error code and error message
    response = jsonify(error.to_dict())
    # response Returns the standard error code defined when the error occurred
    response.status_code = error.status_code
    print(response)

    return response

