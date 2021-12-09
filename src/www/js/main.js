var activeProject = null;
$(document).ready(function () {
    eel.get_projects()(function (projects) {
        $("#projects-body").empty();
        projects.forEach(function (project) {
            $("#projects-body").append("<tr><td>"+project+"</td><td>Unkown</td> <td><button class='activate-button' id='activate-"+project+"'>Activate</button></td></tr>");
        });
        activate_button_On();
    });

    //lista de projetos
    //eel.get_all_projects()(function (projects){});

    //dados do modelo de cada projeto
    //eel.get_list_from_project({});
    //(project)

    //feedback from user, used to update database and model
    eel.receive_feedback (image_id, feedback)((returnVal)=>{
        if(returnVal)alert("sucesso");
         else alert ("falha ao atualizar feedback")})
    
});

function activate_button_On(){
    $(".activate-button").click(function(){
        alert($(this).attr("id").split("-")[1]);
    });
}
