from django.shortcuts import render
from django_ajax.decorators import ajax
from tictack_cmd.game_engine import GameEngine

game_engine = GameEngine()

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
    context = {}
    game_engine.makePlayerStep(cell_index=step_cell_index)
    game_engine.makeComputerStep()

    context['indexes'] = game_engine.game_field_array
    return render(request=request, template_name="game_field_widget.htm", context=context)