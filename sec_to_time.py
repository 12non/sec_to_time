
def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    years = seconds // (60*60*24*365)       
    seconds = seconds % (60*60*24*365)
    days = seconds // (60*60*24)
    seconds = seconds % (60*60*24)
    hours = seconds // (60*60)
    seconds = seconds % (60*60)
    minutes = seconds // 60
    seconds = seconds % 60
    sec = seconds

    result = []
    if years:
        result.append(f"{years} {'year' if years == 1 else 'years'}")
    if days:
        result.append(f"{days} {'day' if days == 1 else 'days'}")
    if hours:
        result.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes:
        result.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if sec:
        result.append(f"{sec} {'second' if sec == 1 else 'seconds'}")

    if len(result) == 1:
        return "".join(result)
    if len(result) == 2:
        return " and ".join(result)
    else:
        return ", ".join(result[:-1]) + " and " + result[-1]
   
#print(format_duration(1264684680))
