from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TestSubject, SleepLevelLog, SingleLog
from django.views.decorators.http import require_http_methods
import json


# Create your views here.
@require_http_methods(["POST"])
def create_test_subject(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    age = body['age']
    gender = body['gender']
    education = body['education']
    occupation = body['occupation']

    subject = TestSubject(age=age, gender=gender,
                          education=education, occupation=occupation)

    subject.save()

    return HttpResponse(subject.get_user_id())


@require_http_methods(["POST"])
def set_sleep_level(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    timestamp = body['timestamp']
    level = body['level']
    user_id = body['userId']

    test_subject = TestSubject.objects.get(userId=user_id)
    sleep_level = SleepLevelLog(sleepLevel=level, testSubject=test_subject, timestamp=timestamp)

    sleep_level.save()

    return HttpResponse("Sleep level saved successfully.")


@require_http_methods(["GET"])
def does_user_exist(request, userid):
    num_users = TestSubject.objects.filter(userId=userid).count()

    if num_users == 1:
        return HttpResponse("Exists")
    else:
        return HttpResponse("Does not exist.")



@require_http_methods(["POST"])
def handle_emotion_data(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    data_string = body['data']
    user_id = body['userId']
    test_subject = TestSubject.objects.get(userId=user_id)

    data_array = data_string.split(' * ')

    data_array = [i for i in data_array if i != '']
    data_array = list(map(json.loads, data_array))

    for log in data_array:
        single_log = SingleLog(testSubject=test_subject, timestamp=log['ts'], smile=log['a'], innerBrowRaise=log['b'],
                              browRaise=log['c'], browFurrow=log['d'], noseWrinkle=log['e'], upperLipRaise=log['f'], lipCornerDepressor=log['g'],
                              chinRaise=log['h'], lipPucker=log['i'], lipPress=log['j'], lipSuck=log['j'], mouthOpen=log['l'],
                              smirk=log['m'], eyeClosure=log['n'], attention=log['o'], lidTighten=log['p'], jawDrop=log['q'],
                              dimpler=log['r'], eyeWiden=log['s'], cheekRaise=log['t'], lipStretch=log['u'] )
        single_log.save()

    # sleep_level.save()

    return HttpResponse("Received data")
