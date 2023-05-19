from rest_framework.views import APIView
from db.organization import UserOrganizationLink
from utils.permission import CustomizePermission, JWTUtils, RoleRequired
from utils.response import CustomResponse
from utils.types import OrganizationType, RoleType
from utils.utils import CommonUtils
from .serializers import CollegeSerializer, UserOrgSerializer


class StudentDetails(APIView):
    authentication_classes = [CustomizePermission]
    @RoleRequired(roles=[RoleType.CAMPUS_AMBASSADOR])
    def get(self, request):
        user_id = JWTUtils.fetch_user_id(request)
        user_org_link = UserOrganizationLink.objects.filter(
            user_id=user_id, org__org_type=OrganizationType.COLLEGE.value).first()
        user_org_links = UserOrganizationLink.objects.filter(
            org_id=user_org_link.org_id)
        paginated_queryset = CommonUtils.get_paginated_queryset(user_org_links, request, ['name'])
        serializer = UserOrgSerializer(paginated_queryset.get('queryset'), many=True)
        serialized_data = serializer.data
        return CustomResponse(response={"data":serialized_data,"pagination":paginated_queryset.get('pagination')}).get_success_response()


class CampusDetails(APIView):
    authentication_classes = [CustomizePermission]
    @RoleRequired(roles=[RoleType.CAMPUS_AMBASSADOR])
    def get(self, request):
        user_id = JWTUtils.fetch_user_id(request)
        user_org_link = UserOrganizationLink.objects.filter(
            user_id=user_id, org__org_type=OrganizationType.COLLEGE.value).first()
        serializer = CollegeSerializer(user_org_link, many=False).data
        return CustomResponse(response=serializer).get_success_response()


