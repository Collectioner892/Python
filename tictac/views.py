from django.shortcuts import render
from django_ajax.decorators import ajax
from tictack_cmd.game_engine import game_engine

# Create your views here.
def home(request):
    # refresh to init
    game_engine.resetGameField()
    context = {
        'game_field_cell_indexes': game_engine.game_field_array,
        'is_winner_defined': (False, "")}
    return render(request=request, template_name="master_page.htm", context=context)

@ajax
def resetGame(request):
    game_engine.resetGameField()

    context = {
        'game_field_cell_indexes': game_engine.game_field_array,
        'is_winner_defined': (False, "")}
    return render(request=request, template_name="game_field_widget.htm", context=context)

@ajax
def handleUserAction(request):
    step_cell_index = int(request.POST['index'])

    game_engine.makePlayerStep(cell_index=step_cell_index)
    is_winner_defined = game_engine.is_defined_winner()

    if is_winner_defined[0]:
        context = {
            'game_field_cell_indexes': game_engine.game_field_array,
            'is_winner_defined': is_winner_defined}
        return render(request=request, template_name="game_field_widget.htm", context=context)

    game_engine.makeComputerStep()
    is_winner_defined = game_engine.is_defined_winner()
    context = {
        'game_field_cell_indexes': game_engine.game_field_array,
        'is_winner_defined': is_winner_defined}
    return render(request=request, template_name="game_field_widget.htm", context=context)