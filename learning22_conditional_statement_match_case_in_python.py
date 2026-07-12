"""Match-Case (alternative of switch)"""
# # Works exactly like switch-case in Dart or C++.
# Used to replace a large ladder of if elif
# (nested if conditions)
status_code = 404

match status_code:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _: # The underscore (_) acts as the default case
        print("Unknow Status")


"""With return type"""
def is_day(s):

    match s:
        case "day":
            return True
        case "night":
            return False
        case _:
            return False

print(is_day("night"))