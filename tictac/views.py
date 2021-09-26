from django.shortcuts import render
from django_ajax.decorators import ajax
from tictack_cmd.game_engine import game_engine

# Create your views here.
def home(request):
    # refresh to init
    game_engine.resetGameField()
    context = {}
    context['indexes'] = game_engine.game_field_array
    return render(request=request, template_name="master_page.htm", context=context)

@ajax
def handleUserAction(request):
    step_cell_index = int(request.POST['index'])
    print("we are here...")
    print(request.POST)
    context = {}
    print(game_engine.game_field_array)
    game_engine.makePlayerStep(cell_index=step_cell_index)
    print(game_engine.game_field_array)
    game_engine.makeComputerStep()
    print(game_engine.game_field_array)
    context['indexes'] = game_engine.game_field_array
    return render(request=request, template_name="game_field_widget.htm", context=context)