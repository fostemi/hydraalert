from django.shortcuts import render
from django.http import HttpResponse

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
