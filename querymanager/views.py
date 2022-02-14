import traceback
import json
from passlib.hash import bcrypt

from django.shortcuts import render,redirect
from django.core import serializers
from django.contrib import messages
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response

from querymanager.models import CompanyData

def make_response(version, response_code, _response_data):
    response_data = {
        'responseCode': response_code,
        'responseFormatVersion': version,
        'responseData': {
            "datatype": "JSON",
            "value": _response_data
        }
    }
    return response_data

def fill_filtersList(filters_list,filterKey,filtersData):
    
   
    for i in filters_list:
        if filterKey in i:
            for elem in filtersData:
                i[filterKey].append(elem[filterKey])

        
    return filters_list

# Create your views here.
@api_view(['GET'])
def getCompanyFilters(request):
    try:
        filters_list=[{'industry':[]},{'year_founded':[]},{'city':[]},{'state':[]},{'country':[]}]

        #fetching distinct industry values
        distinct_industry=CompanyData.objects.values('industry').distinct()
        filters_list=fill_filtersList(filters_list,'industry',distinct_industry)
        
        #fetching distinct year_founded values
        distinct_year_founded=CompanyData.objects.values('year_founded').distinct()
        filters_list=fill_filtersList(filters_list,'year_founded',distinct_year_founded)

        #fetching distinct country values
        distinct_country=CompanyData.objects.values('country').distinct()
        filters_list=fill_filtersList(filters_list,'country',distinct_country)

        #fetching distinct city values
        distinct_city=CompanyData.objects.values('city').distinct()
        filters_list=fill_filtersList(filters_list,'city',distinct_city)

        #fetching distinct state values
        distinct_state=CompanyData.objects.values('state').distinct()
        filters_list=fill_filtersList(filters_list,'state',distinct_state)

        response_payload = make_response('v1', 0, {'companyFilters': { 'value': filters_list}})
       
        return Response(response_payload, 200)
    except :
        traceback.print_exc()
        response_payload = make_response('v1', -1, {'errorMessage': 'Unable to process request'})
        return Response(response_payload, 500)

@api_view(['GET'])
def getQueryCount(request):
    try:
       
        filter_columns=["industry","city","state","country","year_founded"]
        
        if( any(item in filter_columns for item in list(request.query_params.keys()))):
            to_filter_items={}
            for i in filter_columns:
                value=request.query_params[i]
                if value!='Select':
                    to_filter_items[i]=value
            
            query=""
            query = Q()
            
            for key,val in to_filter_items.items():
                if key=="country":
                    query &= Q(country=val)
                elif key=="city":
                    query &= Q(city=val)
                elif key=="state":
                    query &= Q(state=val)
                elif key=="industry":
                    query &= Q(industry=val)
                elif key=="year_founded":
                    query &= Q(year_founded=val)
               
            
           
            count_query = CompanyData.objects.filter(query).count()
            # ticket_query = CompanyData.objects.filter(Q(country="finland")|Q(year_founded=1865)|Q(city='teaneck'))
            print("query count:",count_query)


            response_payload = make_response('v1', 0, {'companyFilters': { 'value': count_query}})
        
            return Response(response_payload, 200)
        else:
            response_payload = make_response('v1', -1, {'errorMessage': 'Nothing to query'})
            return Response(response_payload, 500)

    except :
        traceback.print_exc()
        response_payload = make_response('v1', -1, {'errorMessage': 'Unable to process request'})
        return Response(response_payload, 500)