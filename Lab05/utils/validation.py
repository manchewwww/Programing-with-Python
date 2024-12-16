def validate_arguments(args):
    if len(args) != 4:
        return False

    media_type, time_window, output_format = args[1], args[2], args[3]
    if media_type not in ["tv", "movies", "all"]:
        return False
    if time_window not in ["day", "week"]:
        return False
    if output_format not in ["csv", "json"]:
        return False
    return True
