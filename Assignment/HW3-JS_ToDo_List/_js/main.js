var todo_btn_style = "<a class='waves-effect waves-light btn-tiny green white-text' ";
var todo_btn_id = "id='todo_";
var todo_btn_text = "'> mark complete </a> ";

var completed_btn_style = "<a class='waves-effect waves-light btn-tiny green white-text' ";
var completed_btn_id = "id='completed_";
var completed_btn_text = "'> mark to-do </a> ";

var btn_counter = 0;


function item_remove(item){
    console.log(item + " will be removed");
    $(item).remove();
}

function make_button(type, id){
    if (type == "todo"){
        return (todo_btn_style + todo_btn_id + id + todo_btn_text);
    } else {
        return (completed_btn_style + completed_btn_id + id + completed_btn_text);
    }
}

function make_task(type, id, task_text){
    button = make_button(type, id);
    var tag = "completed_";
    if (type == "todo"){
        tag = "todo_";
    }
    task_id = "<span id='" + tag + "task_" + id + "'>";
    return (button + task_id + task_text + "</p></span>");
}

$(document).ready(
    $("#new-item").on('click', function() {
        next_item = $("input");

        $.each(next_item, function(k, v) {
            btn_counter ++;
            $("#list_todo").prepend(make_task("todo", btn_counter, v.value));
        });
        $('#new_task').val('')
    })
);

$("#list_todo").on('click', ".btn-tiny", function() {
    raw_id = $('.btn-tiny').get(0).id;
    id = raw_id.split("_")[1];

    todo_task = "#todo_task_" + id;
    todo_button = "#" + raw_id;

    task_text = $(todo_task).text();
    $("#list_completed").prepend(make_task("completed", id, task_text));

    item_remove(todo_button);
    item_remove(todo_task);
});


$("#list_completed").on('click', ".btn-tiny", function() {
    raw_id = $('.btn-tiny').get(0).id;
    console.log("raw_id: " + raw_id);
    id = raw_id.split("_")[1];

    completed_task = "#completed_task_" + id;
    completed_button = "#" + raw_id;

    task_text = $(completed_task).text();
    $("#list_todo").prepend(make_task("todo", id, task_text));

    item_remove(completed_button);
    item_remove(completed_task);
});
