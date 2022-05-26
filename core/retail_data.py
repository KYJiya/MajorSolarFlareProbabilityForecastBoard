import re
import datetime


def retail_data(data):
    retailed_data = []
    match_start_datetime = []
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.]\d{1}.+", data)

    while match != None:
        match_data = data[match.regs[0][0] : match.regs[0][1]]
        match_start = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", match_data)

        match_start_datetime.append(
            datetime.datetime.strptime(
                match_data[match_start.regs[0][0] : match_start.regs[0][1]],
                "%Y-%m-%d %H:%M:%S",
            )
        )
        
        retailed_data.append(match_data)

        data = data[match.regs[0][1] :]
        match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.]\d{1}.+", data)

    return retailed_data


def retail_match_start_time(data):    
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.]\d{1}.+", data)
    match_data = data[match.regs[0][0] : match.regs[0][1]]

    match_start = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", match_data)

    match_start_datetime = datetime.datetime.strptime(
        match_data[match_start.regs[0][0] : match_start.regs[0][1]],
        "%Y-%m-%d %H:%M:%S",
    )

    return match_start_datetime