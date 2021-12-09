var activeProject = null;
$(document).ready(function () {
    eel.get_projects()(function (projects) {
        $("#projects-body").empty();
        projects.forEach(function (project) {
            $("#projects-body").append("<tr><td>"+project+"</td><td>Unkown</td> <td><button class='activate-button' id='activate-"+project+"'>Activate</button></td></tr>");
        });
        activate_button_On();
    });

});

function activate_button_On(){
    $(".activate-button").click(function(){
        let project_name = $(this).attr("id").split("-")[1];
        eel.activate_project(project_name)(function(result){
            window.location.href = "project.html?project="+project_name;
        });
    });
}
