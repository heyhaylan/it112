from django.shortcuts import render, get_object_or_404
from .models import Game
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

def api_get_all(request):
    if request.method == 'GET':
        games = Game.objects.all()
        data = [{
            'id': game.id,
            'title': game.title,
            'genre': game.genre,
            'studio': game.studio,
            'release_year': game.release_year
        } for game in games]
        return JsonResponse(data, safe=False, content_type='application/json')
    
def api_get_game_by_id(request):
    if request.method == 'GET':
        game_id = request.GET.get('id')
        if game_id:
            try:
                game = Game.objects.get(id=game_id)
                data = {
                    'id': game.id,
                    'title': game.title,
                    'genre': game.genre,
                    'studio': game.studio,
                    'release_year': game.release_year
                }
                return JsonResponse(data, content_type='application/json')
            except Game.DoesNotExist:
                return JsonResponse({'error': 'Game not found.'}, content_type='application/json')
        return JsonResponse({'error': 'No ID provided.'}, content_type='application/json')

@csrf_exempt
def api_create_game(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            title = body.get('title')
            genre = body.get('genre')
            studio = body.get('studio')
            release_year = body.get('release_year')

            if not all([title, genre, studio, release_year]):
                return JsonResponse({'error': 'Missing fields!'}, content_type='application/json')

            game = Game.objects.create(
                title=title,
                genre=genre,
                studio=studio,
                release_year=release_year
            )

            return JsonResponse({
                'success': True,
                'message': 'Game created!',
                'game': {
                    'id': game.id,
                    'title': game.title,
                    'genre': game.genre,
                    'studio': game.studio,
                    'release_year': game.release_year
                }
            }, content_type='application/json')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, content_type='application/json')
    else:
        return JsonResponse({'error': 'Only POST allowed.'}, content_type='application/json')
