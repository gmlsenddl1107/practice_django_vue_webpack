from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Video, Rating, GpuStatus
from .serializers import VideoSerializer, RatingSerializer, UserSerializer, GpuStatusSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True)
    def rate_video(self, request, pk=None):
        if 'stars' in request.data:
            # response에서 데이터 추출
            video = Video.objects.get(id=pk)
            stars = request.data['stars']
            comments = request.data['comments']
            user = request.user
            try:
                # 이미 있는 경우 DB에서 가져와서 새 내용 넣고 다시 저
                rating = Rating.objects.get(user=user.id, video=video.id)
                rating.stars = stars
                rating.comments = comments
                rating.save()

                # 화면 업데이트를 위해 업데이된 내용 return
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating has been updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                # DB에 없는 경우 새롭게 생성
                rating = Rating.objects.create(user=user, video=video, stars=stars, comments=comments)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            # 잘못 보낸 경
            response = {'message': 'Please enter stars for the rating'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_class = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    # 자동으로 생성되는 delete, create를 막기 위해서
    def delete(self, request, *args, **kwargs):
        response = {'message': 'Rating cannot be updated like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # 자동으로 생성되는 delete, create를 막기 위해서
    def create(self, request, *args, **kwargs):
        response = {'message': 'Rating cannot be created like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
