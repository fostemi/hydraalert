from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, 'calendar/index.html')

def weekdays(request):
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weekday_html = ''.join(f'<th>{day}</th>' for day in weekdays)
    return HttpResponse(weekday_html)

def calendar(request):
    calendar_html = """
    <tbody>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
        </tr>
        <tr>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
        </tr>
    </tbody>
    """
    return HttpResponse(calendar_html)

def get_calendar_body(request):
    month = int(request.GET.get('month', datetime.now().month))
    year = int(request.GET.get('year', datetime.now().year))

    # Create a calendar object
    cal = calendar.monthcalendar(year, month)

    # Generate HTML for the calendar body
    html = ""
    for week in cal:
        html += "<tr>"
        for day in week:
            if day == 0:
                html += '<td class="other-month"></td>'
            elif day == datetime.now().day and month == datetime.now().month and year == datetime.now().year:
                html += f'<td class="today">{day}</td>'
            else:
                html += f'<td>{day}</td>'
        html += "</tr>"

    return HttpResponse(html)

def get_calendar(request):
    # Similar to get_calendar_body, but returns the entire calendar HTML
    # including the month/year header and navigation buttons
    month = int(request.GET.get('month', datetime.now().month))
    year = int(request.GET.get('year', datetime.now().year))

    if request.GET.get('month') == 'prev':
        month -= 1
        if month == 0:
            month = 12
            year -= 1
    elif request.GET.get('month') == 'next':
        month += 1
        if month == 13:
            month = 1
            year += 1

    # Generate the full calendar HTML here
    # ...

    return HttpResponse(full_calendar_html)
