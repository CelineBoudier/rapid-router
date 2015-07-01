from django.http import HttpResponse
from game.models import Level, Episode, LevelBlock, Block, Theme, Character
from game.serializers import LevelListSerializer, EpisodeListSerializer, LevelDetailSerializer, EpisodeDetailSerializer, \
    LevelBlockSerializer, BlockSerializer, ThemeSerializer, CharacterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import generics


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'levels': reverse('level-list', request=request, format=format),
        'episodes': reverse('episode-list', request=request, format=format),
    })


@api_view(('GET',))
def level_list(request, format=None):
    levels = Level.objects.all()
    serializer = LevelListSerializer(levels, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def level_detail(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)


    serializer = LevelDetailSerializer(level, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def episode_list(request, format=None):
    episodes = Episode.objects.all()
    serializer = EpisodeListSerializer(episodes, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def episode_detail(request, pk, format=None):
    try:
        episode = Episode.objects.get(pk=pk)
    except Episode.DoesNotExist:
        return HttpResponse(status=404)

    serializer = EpisodeDetailSerializer(episode, context={'request': request})
    return Response(serializer.data)

@api_view(('GET',))
def levelblock_list(request, level, format=None):
    print level
    blocks = LevelBlock.objects.filter(level__id=level)

    serializer = LevelBlockSerializer(blocks, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def levelblock_detail(request, pk, format=None):
    try:
        levelblock = LevelBlock.objects.get(pk=pk)
    except LevelBlock.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelBlockSerializer(levelblock, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def block_detail(request, pk, format=None):
    try:
        block = Block.objects.get(pk=pk)
    except Block.DoesNotExist:
        return HttpResponse(status=404)

    serializer = BlockSerializer(block, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def theme_detail(request, pk, format=None):
    try:
        theme = Theme.objects.get(pk=pk)
    except Theme.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ThemeSerializer(theme, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def character_detail(request, pk, format=None):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return HttpResponse(status=404)

    serializer = CharacterSerializer(character, context={'request': request})
    return Response(serializer.data)


# Maybe used later for when we use a viewset which requires multiple serializer
class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': None,
        }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])
