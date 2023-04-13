from django.shortcuts import render
from entry_app.models import temp_invtech_info
from invtech.models import invtech_info
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.contrib import messages

from rest_framework.generics import ListAPIView
from entry_app.pagination import StandardResultsSetPagination
from entry_app.serializers import EntappSerializers
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
import shutil
from os import path

from django.http import HttpResponse


def entappv(request):
    if request.method == "POST":
        invtech = request.POST.get("invtech")
        usingarea = request.POST.get("usingarea")
        prov_name = request.POST.get("prov_name")
        prod_name = request.POST.get("prod_name")
        status = request.POST.get("status")

        os.mkdir(os.path.join(settings.STATICFILES_DIRS[0], 'uploads/invtech_files/'+invtech))
        itdir_name = 'uploads/invtech_files/'+invtech

        full_hars = request.FILES['full_hars']
        full_hars_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, full_hars.name)
        with open(full_hars_path, 'wb+') as destination:
            for chunk in full_hars.chunks():
                destination.write(chunk)
        full_hars_fname = full_hars.name

        if 'images' in request.FILES:
            images = request.FILES['images']
            images_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, images.name)
            with open(images_path, 'wb+') as destination:
                for chunk in images.chunks():
                    destination.write(chunk)
            images_fname = images.name
        else:
            images_fname = None
        
        if 'otchet_kazdornii' in request.FILES:
            otchet_kazdornii = request.FILES['otchet_kazdornii']
            otchet_kazdornii_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, otchet_kazdornii.name)
            with open(otchet_kazdornii_path, 'wb+') as destination:
                for chunk in otchet_kazdornii.chunks():
                    destination.write(chunk)
            otchet_kazdornii_fname = otchet_kazdornii.name
        else:
            otchet_kazdornii_fname = None
        
        if 'passport_safety' in request.FILES:
            passport_safety = request.FILES['passport_safety']
            passport_safety_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, passport_safety.name)
            with open(passport_safety_path, 'wb+') as destination:
                for chunk in passport_safety.chunks():
                    destination.write(chunk)
            passport_safety_fname = passport_safety.name
        else:
            passport_safety_fname = None

        if 'rrk' in request.FILES:
            rrk = request.FILES['rrk']
            rrk_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, rrk.name)
            with open(rrk_path, 'wb+') as destination:
                for chunk in rrk.chunks():
                    destination.write(chunk)
            rrk_fname = rrk.name
        else:
            rrk_fname = None

        if 'conclusion_kazdornii' in request.FILES:
            conclusion_kazdornii = request.FILES['conclusion_kazdornii']
            conclusion_kazdornii_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, conclusion_kazdornii.name)
            with open(conclusion_kazdornii_path, 'wb+') as destination:
                for chunk in conclusion_kazdornii.chunks():
                    destination.write(chunk)
            conclusion_kazdornii_fname = conclusion_kazdornii.name
        else:
            conclusion_kazdornii_fname = None

        if 'certification_reference' in request.FILES:
            certification_reference = request.FILES['certification_reference']
            certification_reference_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, certification_reference.name)
            with open(certification_reference_path, 'wb+') as destination:
                for chunk in certification_reference.chunks():
                    destination.write(chunk)
            certification_reference_fname = certification_reference.name
        else:
            certification_reference_fname = None

        if 'quality_certificate' in request.FILES:
            quality_certificate = request.FILES['quality_certificate']
            quality_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, quality_certificate.name)
            with open(quality_certificate_path, 'wb+') as destination:
                for chunk in quality_certificate.chunks():
                    destination.write(chunk)
            quality_certificate_fname = quality_certificate.name
        else:
            quality_certificate_fname = None

        if 'conformity_certificate' in request.FILES:
            conformity_certificate = request.FILES['conformity_certificate']
            conformity_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, conformity_certificate.name)
            with open(conformity_certificate_path, 'wb+') as destination:
                for chunk in conformity_certificate.chunks():
                    destination.write(chunk)
            conformity_certificate_fname = conformity_certificate.name
        else:
            conformity_certificate_fname = None

        if 'lab_conclusion' in request.FILES:
            lab_conclusion = request.FILES['lab_conclusion']
            lab_conclusion_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, lab_conclusion.name)
            with open(lab_conclusion_path, 'wb+') as destination:
                for chunk in lab_conclusion.chunks():
                    destination.write(chunk)
            lab_conclusion_fname = lab_conclusion.name
        else:
            lab_conclusion_fname = None

        if 'ses_expert_conclusion' in request.FILES:
            ses_expert_conclusion = request.FILES['ses_expert_conclusion']
            ses_expert_conclusion_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, ses_expert_conclusion.name)
            with open(ses_expert_conclusion_path, 'wb+') as destination:
                for chunk in ses_expert_conclusion.chunks():
                    destination.write(chunk)
            ses_expert_conclusion_fname = ses_expert_conclusion.name
        else:
            ses_expert_conclusion_fname = None

        if 'state_registration_certificate' in request.FILES:
            state_registration_certificate = request.FILES['state_registration_certificate']
            state_registration_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, state_registration_certificate.name)
            with open(state_registration_certificate_path, 'wb+') as destination:
                for chunk in state_registration_certificate.chunks():
                    destination.write(chunk)
            state_registration_certificate_fname = state_registration_certificate.name
        else:
            state_registration_certificate_fname = None

        if 'akt' in request.FILES:
            akt = request.FILES['akt']
            akt_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, akt.name)
            with open(akt_path, 'wb+') as destination:
                for chunk in akt.chunks():
                    destination.write(chunk)
            akt_fname = akt.name
        else:
            akt_fname = None

        if 'addition' in request.FILES:
            addition = request.FILES['addition']
            addition_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, addition.name)
            with open(addition_path, 'wb+') as destination:
                for chunk in addition.chunks():
                    destination.write(chunk)
            addition_fname = addition.name
        else:
            addition_fname = None

        lname = request.POST.get("lname")
        fname = request.POST.get("fname")
        dname = request.POST.get("dname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        tempinvtech_instance = temp_invtech_info(
            invtech=invtech,
            usingarea=usingarea,
            prov_name=prov_name,
            prod_name=prod_name,
            status=status,
            images=images_fname,
            full_hars=full_hars_fname,
            otchet_kazdornii=otchet_kazdornii_fname,
            passport_safety=passport_safety_fname,
            rrk=rrk_fname,
            conclusion_kazdornii=conclusion_kazdornii_fname,
            certification_reference=certification_reference_fname,
            quality_certificate=quality_certificate_fname,
            conformity_certificate=conformity_certificate_fname,
            lab_conclusion=lab_conclusion_fname,
            ses_expert_conclusion=ses_expert_conclusion_fname,
            state_registration_certificate=state_registration_certificate_fname,
            akt=akt_fname,
            addition = addition_fname,
            lname=lname,
            fname=fname,
            dname=dname,
            email=email,
            phone=phone,
            entapp_status='новая',
            sent_status='в ожиданий')
        tempinvtech_instance.save()
        messages.success(request, 'Заявка успешно отправлена!')
    return render(request, 'entry_app/entapp_form.html')


def entappv_edit(request):
    pptit_id2 = request.COOKIES.get('pptit_id2')
    print("pptit_id2 = ", pptit_id2)
    
    ppit_id2 = request.COOKIES.get('ppit_id2')
    print("ppit_id2 = ", ppit_id2)

    if pptit_id2 != None and pptit_id2 != '-1':
        temp_invtech_instance = temp_invtech_info.objects.get(it_id=pptit_id2)

        context = {
            'prov_name': temp_invtech_instance.prov_name,
            'prod_name': temp_invtech_instance.prod_name,
            'invtech': temp_invtech_instance.invtech,
            'usingarea': temp_invtech_instance.usingarea,
            'status': temp_invtech_instance.status,
        }

        if request.method == "POST":
            invtech = request.POST.get("invtech")
            usingarea = request.POST.get("usingarea")
            prov_name = request.POST.get("prov_name")
            prod_name = request.POST.get("prod_name")
            status = request.POST.get("status")
            
            if temp_invtech_instance.sent_status == 'в ожиданий':
                spath_itfiles = os.path.join(settings.STATICFILES_DIRS[0], 'uploads/invtech_files/', temp_invtech_instance.invtech)
                shutil.rmtree(spath_itfiles)

            os.mkdir(os.path.join(settings.STATICFILES_DIRS[0], 'uploads/invtech_files/'+invtech))
            itdir_name = 'uploads/invtech_files/'+invtech

            full_hars = request.FILES['full_hars']
            full_hars_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, full_hars.name)
            with open(full_hars_path, 'wb+') as destination:
                for chunk in full_hars.chunks():
                    destination.write(chunk)
            full_hars_fname = full_hars.name

            if 'images' in request.FILES:
                images = request.FILES['images']
                images_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, images.name)
                with open(images_path, 'wb+') as destination:
                    for chunk in images.chunks():
                        destination.write(chunk)
                images_fname = images.name
            else:
                images_fname = None
            
            if 'otchet_kazdornii' in request.FILES:
                otchet_kazdornii = request.FILES['otchet_kazdornii']
                otchet_kazdornii_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, otchet_kazdornii.name)
                with open(otchet_kazdornii_path, 'wb+') as destination:
                    for chunk in otchet_kazdornii.chunks():
                        destination.write(chunk)
                otchet_kazdornii_fname = otchet_kazdornii.name
            else:
                otchet_kazdornii_fname = None
            
            if 'passport_safety' in request.FILES:
                passport_safety = request.FILES['passport_safety']
                passport_safety_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, passport_safety.name)
                with open(passport_safety_path, 'wb+') as destination:
                    for chunk in passport_safety.chunks():
                        destination.write(chunk)
                passport_safety_fname = passport_safety.name
            else:
                passport_safety_fname = None

            if 'rrk' in request.FILES:
                rrk = request.FILES['rrk']
                rrk_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, rrk.name)
                with open(rrk_path, 'wb+') as destination:
                    for chunk in rrk.chunks():
                        destination.write(chunk)
                rrk_fname = rrk.name
            else:
                rrk_fname = None

            if 'conclusion_kazdornii' in request.FILES:
                conclusion_kazdornii = request.FILES['conclusion_kazdornii']
                conclusion_kazdornii_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, conclusion_kazdornii.name)
                with open(conclusion_kazdornii_path, 'wb+') as destination:
                    for chunk in conclusion_kazdornii.chunks():
                        destination.write(chunk)
                conclusion_kazdornii_fname = conclusion_kazdornii.name
            else:
                conclusion_kazdornii_fname = None

            if 'certification_reference' in request.FILES:
                certification_reference = request.FILES['certification_reference']
                certification_reference_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, certification_reference.name)
                with open(certification_reference_path, 'wb+') as destination:
                    for chunk in certification_reference.chunks():
                        destination.write(chunk)
                certification_reference_fname = certification_reference.name
            else:
                certification_reference_fname = None

            if 'quality_certificate' in request.FILES:
                quality_certificate = request.FILES['quality_certificate']
                quality_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, quality_certificate.name)
                with open(quality_certificate_path, 'wb+') as destination:
                    for chunk in quality_certificate.chunks():
                        destination.write(chunk)
                quality_certificate_fname = quality_certificate.name
            else:
                quality_certificate_fname = None

            if 'conformity_certificate' in request.FILES:
                conformity_certificate = request.FILES['conformity_certificate']
                conformity_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, conformity_certificate.name)
                with open(conformity_certificate_path, 'wb+') as destination:
                    for chunk in conformity_certificate.chunks():
                        destination.write(chunk)
                conformity_certificate_fname = conformity_certificate.name
            else:
                conformity_certificate_fname = None

            if 'lab_conclusion' in request.FILES:
                lab_conclusion = request.FILES['lab_conclusion']
                lab_conclusion_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, lab_conclusion.name)
                with open(lab_conclusion_path, 'wb+') as destination:
                    for chunk in lab_conclusion.chunks():
                        destination.write(chunk)
                lab_conclusion_fname = lab_conclusion.name
            else:
                lab_conclusion_fname = None

            if 'ses_expert_conclusion' in request.FILES:
                ses_expert_conclusion = request.FILES['ses_expert_conclusion']
                ses_expert_conclusion_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, ses_expert_conclusion.name)
                with open(ses_expert_conclusion_path, 'wb+') as destination:
                    for chunk in ses_expert_conclusion.chunks():
                        destination.write(chunk)
                ses_expert_conclusion_fname = ses_expert_conclusion.name
            else:
                ses_expert_conclusion_fname = None

            if 'state_registration_certificate' in request.FILES:
                state_registration_certificate = request.FILES['state_registration_certificate']
                state_registration_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, state_registration_certificate.name)
                with open(state_registration_certificate_path, 'wb+') as destination:
                    for chunk in state_registration_certificate.chunks():
                        destination.write(chunk)
                state_registration_certificate_fname = state_registration_certificate.name
            else:
                state_registration_certificate_fname = None

            if 'akt' in request.FILES:
                akt = request.FILES['akt']
                akt_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, akt.name)
                with open(akt_path, 'wb+') as destination:
                    for chunk in akt.chunks():
                        destination.write(chunk)
                akt_fname = akt.name
            else:
                akt_fname = None

            if 'addition' in request.FILES:
                addition = request.FILES['addition']
                addition_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, addition.name)
                with open(addition_path, 'wb+') as destination:
                    for chunk in addition.chunks():
                        destination.write(chunk)
                addition_fname = addition.name
            else:
                addition_fname = None

            lname = request.POST.get("lname")
            fname = request.POST.get("fname")
            dname = request.POST.get("dname")
            email = request.POST.get("email")
            phone = request.POST.get("phone")

            temp_invtech_instance.invtech = invtech
            temp_invtech_instance.usingarea = usingarea
            temp_invtech_instance.prov_name = prov_name
            temp_invtech_instance.prod_name = prod_name
            temp_invtech_instance.status = status
            temp_invtech_instance.images = images_fname
            temp_invtech_instance.full_hars = full_hars_fname
            temp_invtech_instance.otchet_kazdornii = otchet_kazdornii_fname
            temp_invtech_instance.passport_safety = passport_safety_fname
            temp_invtech_instance.rrk = rrk_fname
            temp_invtech_instance.conclusion_kazdornii = conclusion_kazdornii_fname
            temp_invtech_instance.certification_reference = certification_reference_fname
            temp_invtech_instance.quality_certificate = quality_certificate_fname
            temp_invtech_instance.conformity_certificate = conformity_certificate_fname
            temp_invtech_instance.lab_conclusion = lab_conclusion_fname
            temp_invtech_instance.ses_expert_conclusion = ses_expert_conclusion_fname
            temp_invtech_instance.state_registration_certificate = state_registration_certificate_fname
            temp_invtech_instance.akt = akt_fname
            temp_invtech_instance.addition = addition_fname
            temp_invtech_instance.lname = lname
            temp_invtech_instance.fname = fname
            temp_invtech_instance.dname = dname
            temp_invtech_instance.email = email
            temp_invtech_instance.phone = phone
            temp_invtech_instance.entapp_status = 'новая'
            temp_invtech_instance.sent_status = 'в ожиданий'
            temp_invtech_instance.save()
            messages.success(request, 'Заявка успешно отправлена!')


    elif ppit_id2 != None and ppit_id2 != '-1':
        invtech_instance = invtech_info.objects.get(it_id=ppit_id2)
        fkid = invtech_instance.it_id
        print('fkid = ', fkid)
        
        context = {
            'prov_name': invtech_instance.prov_name,
            'prod_name': invtech_instance.prod_name,
            'invtech': invtech_instance.invtech,
            'usingarea': invtech_instance.usingarea,
            'status': invtech_instance.status,
        }

        
        if request.method == "POST":
            invtech = request.POST.get("invtech")
            usingarea = request.POST.get("usingarea")
            prov_name = request.POST.get("prov_name")
            prod_name = request.POST.get("prod_name")
            status = request.POST.get("status")

            os.mkdir(os.path.join(settings.STATICFILES_DIRS[0], 'uploads/invtech_files/'+invtech))
            itdir_name = 'uploads/invtech_files/'+invtech

            full_hars = request.FILES['full_hars']
            full_hars_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, full_hars.name)
            with open(full_hars_path, 'wb+') as destination:
                for chunk in full_hars.chunks():
                    destination.write(chunk)
            full_hars_fname = full_hars.name

            if 'images' in request.FILES:
                images = request.FILES['images']
                images_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, images.name)
                with open(images_path, 'wb+') as destination:
                    for chunk in images.chunks():
                        destination.write(chunk)
                images_fname = images.name
            else:
                images_fname = None
            
            if 'otchet_kazdornii' in request.FILES:
                otchet_kazdornii = request.FILES['otchet_kazdornii']
                otchet_kazdornii_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, otchet_kazdornii.name)
                with open(otchet_kazdornii_path, 'wb+') as destination:
                    for chunk in otchet_kazdornii.chunks():
                        destination.write(chunk)
                otchet_kazdornii_fname = otchet_kazdornii.name
            else:
                otchet_kazdornii_fname = None
            
            if 'passport_safety' in request.FILES:
                passport_safety = request.FILES['passport_safety']
                passport_safety_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, passport_safety.name)
                with open(passport_safety_path, 'wb+') as destination:
                    for chunk in passport_safety.chunks():
                        destination.write(chunk)
                passport_safety_fname = passport_safety.name
            else:
                passport_safety_fname = None

            if 'rrk' in request.FILES:
                rrk = request.FILES['rrk']
                rrk_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, rrk.name)
                with open(rrk_path, 'wb+') as destination:
                    for chunk in rrk.chunks():
                        destination.write(chunk)
                rrk_fname = rrk.name
            else:
                rrk_fname = None

            if 'conclusion_kazdornii' in request.FILES:
                conclusion_kazdornii = request.FILES['conclusion_kazdornii']
                conclusion_kazdornii_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, conclusion_kazdornii.name)
                with open(conclusion_kazdornii_path, 'wb+') as destination:
                    for chunk in conclusion_kazdornii.chunks():
                        destination.write(chunk)
                conclusion_kazdornii_fname = conclusion_kazdornii.name
            else:
                conclusion_kazdornii_fname = None

            if 'certification_reference' in request.FILES:
                certification_reference = request.FILES['certification_reference']
                certification_reference_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, certification_reference.name)
                with open(certification_reference_path, 'wb+') as destination:
                    for chunk in certification_reference.chunks():
                        destination.write(chunk)
                certification_reference_fname = certification_reference.name
            else:
                certification_reference_fname = None

            if 'quality_certificate' in request.FILES:
                quality_certificate = request.FILES['quality_certificate']
                quality_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, quality_certificate.name)
                with open(quality_certificate_path, 'wb+') as destination:
                    for chunk in quality_certificate.chunks():
                        destination.write(chunk)
                quality_certificate_fname = quality_certificate.name
            else:
                quality_certificate_fname = None

            if 'conformity_certificate' in request.FILES:
                conformity_certificate = request.FILES['conformity_certificate']
                conformity_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, conformity_certificate.name)
                with open(conformity_certificate_path, 'wb+') as destination:
                    for chunk in conformity_certificate.chunks():
                        destination.write(chunk)
                conformity_certificate_fname = conformity_certificate.name
            else:
                conformity_certificate_fname = None

            if 'lab_conclusion' in request.FILES:
                lab_conclusion = request.FILES['lab_conclusion']
                lab_conclusion_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, lab_conclusion.name)
                with open(lab_conclusion_path, 'wb+') as destination:
                    for chunk in lab_conclusion.chunks():
                        destination.write(chunk)
                lab_conclusion_fname = lab_conclusion.name
            else:
                lab_conclusion_fname = None

            if 'ses_expert_conclusion' in request.FILES:
                ses_expert_conclusion = request.FILES['ses_expert_conclusion']
                ses_expert_conclusion_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, ses_expert_conclusion.name)
                with open(ses_expert_conclusion_path, 'wb+') as destination:
                    for chunk in ses_expert_conclusion.chunks():
                        destination.write(chunk)
                ses_expert_conclusion_fname = ses_expert_conclusion.name
            else:
                ses_expert_conclusion_fname = None

            if 'state_registration_certificate' in request.FILES:
                state_registration_certificate = request.FILES['state_registration_certificate']
                state_registration_certificate_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, state_registration_certificate.name)
                with open(state_registration_certificate_path, 'wb+') as destination:
                    for chunk in state_registration_certificate.chunks():
                        destination.write(chunk)
                state_registration_certificate_fname = state_registration_certificate.name
            else:
                state_registration_certificate_fname = None

            if 'akt' in request.FILES:
                akt = request.FILES['akt']
                akt_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, akt.name)
                with open(akt_path, 'wb+') as destination:
                    for chunk in akt.chunks():
                        destination.write(chunk)
                akt_fname = akt.name
            else:
                akt_fname = None

            if 'addition' in request.FILES:
                addition = request.FILES['addition']
                addition_path = os.path.join(settings.STATICFILES_DIRS[0], itdir_name, addition.name)
                with open(addition_path, 'wb+') as destination:
                    for chunk in addition.chunks():
                        destination.write(chunk)
                addition_fname = addition.name
            else:
                addition_fname = None

            lname = request.POST.get("lname")
            fname = request.POST.get("fname")
            dname = request.POST.get("dname")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            temp_invtech_instance = temp_invtech_info(
                invtech=invtech,
                usingarea=usingarea,
                prov_name=prov_name,
                prod_name=prod_name,
                status=status,
                images=images_fname,
                full_hars=full_hars_fname,
                otchet_kazdornii=otchet_kazdornii_fname,
                passport_safety=passport_safety_fname,
                rrk=rrk_fname,
                conclusion_kazdornii=conclusion_kazdornii_fname,
                certification_reference=certification_reference_fname,
                quality_certificate=quality_certificate_fname,
                conformity_certificate=conformity_certificate_fname,
                lab_conclusion=lab_conclusion_fname,
                ses_expert_conclusion=ses_expert_conclusion_fname,
                state_registration_certificate=state_registration_certificate_fname,
                akt=akt_fname,
                addition = addition_fname,
                fkid=fkid,
                lname=lname,
                fname=fname,
                dname=dname,
                email=email,
                phone=phone,
                entapp_status='на редактирование',
                sent_status='в ожиданий')
            temp_invtech_instance.save()
            messages.success(request, 'Заявка успешно отправлена!')

    return render(request, 'entry_app/entapp_form_edit.html', context)


def entapp_list(request):
    return render(request, 'entry_app/entapp_list.html', {})


class EntappListing(ListAPIView):
    # установить класс нумерации страниц и сериализатора
    pagination_class = StandardResultsSetPagination
    serializer_class = EntappSerializers

    def get_queryset(self):
        # фильтровать набор запросов на основе примененных фильтров
        queryList = temp_invtech_info.objects.all()
        sent_status = self.request.query_params.get('sent_status', None)
        entapp_status = self.request.query_params.get('entapp_status', None)
        sort_by = self.request.query_params.get('sort_by', None)
        search = self.request.query_params.get('search', None)

        if search:
            queryList = queryList.filter(
                Q(invtech__icontains=search) |
                Q(prov_name__icontains=search) |
                Q(prod_name__icontains=search) |
                Q(fname__icontains=search)
            )

        if sent_status:
            queryList = queryList.filter(sent_status=sent_status)
        if entapp_status:
            queryList = queryList.filter(entapp_status=entapp_status)

        if sort_by == "by_sent_status":
            queryList = queryList.order_by("sent_status")
        elif sort_by == "by_entapp_status":
            queryList = queryList.order_by("entapp_status")

        return queryList


def getSentStatus(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        sent_status = temp_invtech_info.objects.filter().order_by('sent_status').values_list('sent_status').distinct()
        # print("sent_status = ", sent_status)
        sent_status = [i[0] for i in list(sent_status)]
        data = {
            "sent_status": sent_status,
        }
        return JsonResponse(data, status=200)


def getEntappStatus(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        entapp_status = temp_invtech_info.objects.filter().order_by('entapp_status').values_list('entapp_status').distinct()
        # print("entapp_status = ", entapp_status)
        entapp_status = [i[0] for i in list(entapp_status)]
        data = {
            "entapp_status": entapp_status,
        }
        return JsonResponse(data, status=200)


def entapp_invtech(request):
    linkea = request.COOKIES.get('linkea')
    #print("linkea = ", linkea)
    appits = temp_invtech_info.objects.filter(it_id=linkea)
    #print('appits = ', appits)
    filename = temp_invtech_info.objects.filter(it_id=linkea).values_list('full_hars', flat=True)[0]
    itfile = temp_invtech_info.objects.filter(it_id=linkea).values_list('invtech', flat=True)[0]
    pdffile = os.path.join('/static/uploads/invtech_files/', itfile + '/' + filename)
    #print(pdffile)

    images = appits.first().images
    image_list = []
    if images is not None:
        image_list = images.split(',') if ',' in images else [images]
        for i in range(len(image_list)):
            image = '/static/uploads/invtech_files/' + itfile + '/' + image_list[i]
            image_list[i] = image

    '''
    otchet_kazdornii = appits.first().otchet_kazdornii
    passport_safety = appits.first().passport_safety
    rrk = appits.first().rrk
    conclusion_kazdornii = appits.first().conclusion_kazdornii
    certification_reference = appits.first().certification_reference
    quality_certificate = appits.first().quality_certificate
    conformity_certificate = appits.first().conformity_certificate
    lab_conclusion = appits.first().lab_conclusion
    ses_expert_conclusion = appits.first().ses_expert_conclusion
    state_registration_certificate = appits.first().state_registration_certificate
    akt = appits.first().akt
    addition = appits.first().addition
    '''

    context = {
        'appits': appits,
        'image_list': image_list,
        'pdffile': pdffile,
    }

    itid_acc = request.POST.get('itid_acc', None)
    print("itid_acc = ", itid_acc)
    itid_rej = request.POST.get('itid_rej', None)
    print("itid_rej = ", itid_rej)
    rej_comment = request.POST.get('rej_comment', None)
    print("rej_comment = ", rej_comment)
    
    if itid_acc != None:
        print('For accept')
        temp_invtech = get_object_or_404(temp_invtech_info, it_id=itid_acc)
        if temp_invtech.entapp_status == 'на редактирование':
            print('For accept --- на редактирование')
            print('fk_id --- ', temp_invtech.fkid)
            invtech_instance = invtech_info.objects.get(it_id=temp_invtech.fkid)
            print('it_id --- ', invtech_instance.it_id)

            spath_itfiles = os.path.join(settings.STATICFILES_DIRS[0], 'files/invtech_files/', invtech_instance.invtech)
            shutil.rmtree(spath_itfiles)

            invtech_instance.invtech = temp_invtech.invtech
            invtech_instance.usingarea = temp_invtech.usingarea
            invtech_instance.prov_name = temp_invtech.prov_name
            invtech_instance.prod_name = temp_invtech.prod_name
            invtech_instance.status = temp_invtech.status
            invtech_instance.images = temp_invtech.images
            invtech_instance.full_hars = temp_invtech.full_hars
            invtech_instance.otchet_kazdornii = temp_invtech.otchet_kazdornii
            invtech_instance.passport_safety = temp_invtech.passport_safety
            invtech_instance.rrk = temp_invtech.rrk
            invtech_instance.conclusion_kazdornii = temp_invtech.conclusion_kazdornii
            invtech_instance.certification_reference = temp_invtech.certification_reference
            invtech_instance.quality_certificate = temp_invtech.quality_certificate
            invtech_instance.conformity_certificate = temp_invtech.conformity_certificate
            invtech_instance.lab_conclusion = temp_invtech.lab_conclusion
            invtech_instance.ses_expert_conclusion = temp_invtech.ses_expert_conclusion
            invtech_instance.state_registration_certificate = temp_invtech.state_registration_certificate
            invtech_instance.akt = temp_invtech.akt
            invtech_instance.addition = temp_invtech.addition
            invtech_instance.save()
            
            spath_itfiles = os.path.join(settings.STATICFILES_DIRS[0], 'uploads/invtech_files/', temp_invtech.invtech)
            dpath_itfiles = os.path.join(settings.STATICFILES_DIRS[0], 'files/invtech_files/', invtech_instance.invtech)
            shutil.move(spath_itfiles, dpath_itfiles)
            
        else:
            invtech_instance = invtech_info(
                invtech = temp_invtech.invtech,
                usingarea = temp_invtech.usingarea,
                prov_name = temp_invtech.prov_name,
                prod_name = temp_invtech.prod_name,
                status = temp_invtech.status,
                images = temp_invtech.images,
                full_hars = temp_invtech.full_hars,
                otchet_kazdornii = temp_invtech.otchet_kazdornii,
                passport_safety = temp_invtech.passport_safety,
                rrk = temp_invtech.rrk,
                conclusion_kazdornii = temp_invtech.conclusion_kazdornii,
                certification_reference = temp_invtech.certification_reference,
                quality_certificate = temp_invtech.quality_certificate,
                conformity_certificate = temp_invtech.conformity_certificate,
                lab_conclusion = temp_invtech.lab_conclusion,
                ses_expert_conclusion = temp_invtech.ses_expert_conclusion,
                state_registration_certificate = temp_invtech.state_registration_certificate,
                akt = temp_invtech.akt
            )
            invtech_instance.save()
            
            '''
            spath_images = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.images) if temp_invtech.images is not None else ''
            spath_full_hars = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.full_hars)
            spath_otchet_kazdornii = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.otchet_kazdornii) if temp_invtech.otchet_kazdornii is not None else ''
            spath_passport_safety = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.passport_safety) if temp_invtech.passport_safety is not None else ''
            spath_rrk = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.rrk) if temp_invtech.rrk is not None else ''
            spath_conclusion_kazdornii = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.conclusion_kazdornii) if temp_invtech.conclusion_kazdornii is not None else ''
            spath_certification_reference = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.certification_reference) if temp_invtech.certification_reference is not None else ''
            spath_quality_certificate = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.quality_certificate) if temp_invtech.quality_certificate is not None else ''
            spath_conformity_certificate = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.conformity_certificate) if temp_invtech.conformity_certificate is not None else ''
            spath_lab_conclusion = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.lab_conclusion) if temp_invtech.lab_conclusion is not None else ''
            spath_ses_expert_conclusion = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.ses_expert_conclusion) if temp_invtech.ses_expert_conclusion is not None else ''
            spath_state_registration_certificate = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.state_registration_certificate) if temp_invtech.state_registration_certificate is not None else ''
            spath_akt = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.akt) if temp_invtech.akt is not None else ''

            files_name = [temp_invtech.images, temp_invtech.full_hars, temp_invtech.otchet_kazdornii, temp_invtech.passport_safety, temp_invtech.rrk,
                        temp_invtech.conclusion_kazdornii, temp_invtech.certification_reference, temp_invtech.quality_certificate, 
                        temp_invtech.conformity_certificate, temp_invtech.lab_conclusion, temp_invtech.ses_expert_conclusion, 
                        temp_invtech.state_registration_certificate, temp_invtech.akt]
            
            files_spath = [spath_images, spath_full_hars, spath_otchet_kazdornii, spath_passport_safety, spath_rrk, 
                        spath_conclusion_kazdornii, spath_certification_reference, spath_quality_certificate, 
                        spath_conformity_certificate, spath_lab_conclusion, spath_ses_expert_conclusion, 
                        spath_state_registration_certificate, spath_akt]
            
            for file_spath, file_name in zip(files_spath, files_name):
                if path.exists(file_spath):
                    destination_path = os.path.join(settings.STATICFILES_DIRS[0], 'files', file_name)
                    shutil.move(file_spath, destination_path)'''
            spath_itfiles = os.path.join(settings.STATICFILES_DIRS[0], 'uploads/invtech_files/', temp_invtech.invtech)
            dpath_itfiles = os.path.join(settings.STATICFILES_DIRS[0], 'files/invtech_files/', temp_invtech.invtech)
            shutil.move(spath_itfiles, dpath_itfiles)

        temp_invtech.delete()
        response_data = {"message": "Заявка принята!"}
        return JsonResponse(response_data)

    elif itid_rej != None and rej_comment != None:
        temp_invtech = get_object_or_404(temp_invtech_info, it_id=itid_rej)
        if temp_invtech.sent_status == 'в ожиданий':
            print('For reject')
            temp_invtech.sent_status = 'отклонено'
            temp_invtech.comments = rej_comment

            '''
            spath_images = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.images) if temp_invtech.images is not None else ''
            spath_full_hars = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.full_hars)
            spath_otchet_kazdornii = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.otchet_kazdornii) if temp_invtech.otchet_kazdornii is not None else ''
            spath_passport_safety = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.passport_safety) if temp_invtech.passport_safety is not None else ''
            spath_rrk = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.rrk) if temp_invtech.rrk is not None else ''
            spath_conclusion_kazdornii = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.conclusion_kazdornii) if temp_invtech.conclusion_kazdornii is not None else ''
            spath_certification_reference = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.certification_reference) if temp_invtech.certification_reference is not None else ''
            spath_quality_certificate = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.quality_certificate) if temp_invtech.quality_certificate is not None else ''
            spath_conformity_certificate = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.conformity_certificate) if temp_invtech.conformity_certificate is not None else ''
            spath_lab_conclusion = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.lab_conclusion) if temp_invtech.lab_conclusion is not None else ''
            spath_ses_expert_conclusion = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.ses_expert_conclusion) if temp_invtech.ses_expert_conclusion is not None else ''
            spath_state_registration_certificate = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.state_registration_certificate) if temp_invtech.state_registration_certificate is not None else ''
            spath_akt = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', temp_invtech.akt) if temp_invtech.akt is not None else ''
            
            files_name = [temp_invtech.images, temp_invtech.full_hars, temp_invtech.otchet_kazdornii, temp_invtech.passport_safety, temp_invtech.rrk,
                        temp_invtech.conclusion_kazdornii, temp_invtech.certification_reference, temp_invtech.quality_certificate, 
                        temp_invtech.conformity_certificate, temp_invtech.lab_conclusion, temp_invtech.ses_expert_conclusion, 
                        temp_invtech.state_registration_certificate, temp_invtech.akt]
            
            files_spath = [spath_images, spath_full_hars, spath_otchet_kazdornii, spath_passport_safety, spath_rrk, 
                        spath_conclusion_kazdornii, spath_certification_reference, spath_quality_certificate, 
                        spath_conformity_certificate, spath_lab_conclusion, spath_ses_expert_conclusion, 
                        spath_state_registration_certificate, spath_akt]
            
            for file_spath, file_name in zip(files_spath, files_name):
                if path.exists(file_spath):
                    file_path = os.path.join(settings.STATICFILES_DIRS[0], 'uploads', file_name)
                    os.remove(file_path)'''

            spath_itfiles = os.path.join(settings.STATICFILES_DIRS[0], 'uploads/invtech_files/', temp_invtech.invtech)
            shutil.rmtree(spath_itfiles)

            temp_invtech.images = None
            temp_invtech.otchet_kazdornii = None
            temp_invtech.passport_safety = None
            temp_invtech.rrk = None
            temp_invtech.conclusion_kazdornii = None
            temp_invtech.certification_reference = None
            temp_invtech.quality_certificate = None
            temp_invtech.conformity_certificate = None
            temp_invtech.lab_conclusion = None
            temp_invtech.ses_expert_conclusion = None
            temp_invtech.state_registration_certificate = None
            temp_invtech.akt = None
            temp_invtech.save()

            response_data = {"message": "Заявка отклонена!"}
            return JsonResponse(response_data)

    else:
        return render(request, 'entry_app/entapp.html', context)


