var project;
var models = [];
var selected_model = "";
var selected_image = "";
$(document).ready(function () {
    project = getUrlParameter('project');
    update_model_list();
    create_model();
    /*eel.get_project_data(project)(function (data) {
        
    });*/
});

function create_model() {
    $("#create-model").click(function (e) { 
        alert("create model");
        eel.create_model()(function (data) {
            if(data){
                update_model_list();
                alert("Model created successfully");
            }
        });
    });
}


function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return typeof sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};

function update_model_list(){
    eel.get_models()(function (data) {
        $("#model-status-table").empty();
        for (var i = 0; i < data.length; i++) {
            models = data;
            if(data[i].number_of_rights+data[i].number_of_wrongs!=0)
                var percentage = (data[i].number_of_rights/(data[i].number_of_rights+data[i].number_of_wrongs))*100;
            else
                var percentage = "TBD";
            $("#model-status-table").append('<tr>'+
                '<td class="model-name">'+data[i].name+'</td>'+
                '<td class="model-status">'+percentage+'</td>'+
                '<td class=""><button type="button" class="btn btn-primary model-activate" id="activate-model'+i+'">Activate</button></td>'+
            '</tr>'
            );
        }
        $("#model-status-table").append("<tr>"+
            '<td colspan="3" style="text-align: center;"><button type="button" class="btn btn-primary" id="create-model">Create Model</button></td>'+
        '</tr>');
        
        create_model();
        update_images();
    });
}

function update_images(){
    $(".model-activate").click(function (e) {
        let i = $(this).attr("id").split("activate-model")[1];
        i = parseInt(i);
        selected_model = i;
        let model = models[i];
        let loading = '<tr>'+
                            '<td colspan="3" style="text-align: center;"><h1>Loading...</h1></td>'+
                        '</tr>';
        $("#project-status-list").empty();
        $("#project-status-list").append(loading);
        
        
        eel.activate_model(model.name)(function (data) {
            if(data){
                $("#project-status-list").empty();
                alert("Model activated successfully");

                

                for(var j = 0; j < model.file_list.length; j++){
                    $("#project-status-list").append(
                        '<tr style="text-align:center" class="project-status" id="'+model.file_list[j].file+'">'+
                            '<td style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis; width: 30vw; background-color: darkgray;">'+model.file_list[j].file+'</td>'+
                            '<td>TBD</td>'+
                            '<td style="background-color: darkgray;">TBD</td>'+
                        '</tr>'
                    );
                }

                $(".project-status").click(function (e) {
                    let file = $(this).attr("id");
                    
        
                    eel.get_image(file)(function (data) {
                        $("#before").attr('src', 'data:image/png;base64,'+data.before);
                        $("#after").attr('src', 'data:image/png;base64,'+data.after);
                        selected_image = file;
                        
                    });
                    $(".modal-img").show();
                });
            }
            else{
                alert("Error in activating model");
            }
        });
        
        

        
    });
}

$(document).ready(function () {
    $(".close").click(function (e) {
        close();
    });

    $("#yes").click(function (e) { 
        update_image(selected_image, true);
        close();
    });
    $("#no").click(function (e) {
        update_image(selected_image, false);
        close();
    });
});

function close(){
    $(".modal-img").hide();
    
    $("#before").attr('src', '');
    $("#after").attr('src', '');
    selected_image = "";
}

function update_image(image, val){
    eel.update_image(image, val)(function (data) {
        if(data){
            update_model_list();
            alert("Image updated successfully");
        }else{
            alert("Error in updating image");
        }
    });
}


function update_image_list(data){
    if(data){
        models[selected_model] = data;
        $("#project-status-list").empty();
        alert("Refreshed successfully");

        

        for(var j = 0; j < data.file_list.length; j++){
            let eval = data.file_list[j].evaluation;
            let result_eval = "TBD";
            let color = "darkgray";
            if( eval != -1) if (Math.abs(eval) < 0.2) {
                result_eval = "Uncertain";
                color = "orange";
            }
            else if (eval > 0.2) {
                result_eval = "Certain True Positive";
                color = "lightcyan";
            }
            else if (eval < -0.2) {
                result_eval = "Certain False Positive";
                color = "lightred";
            }
            $("#project-status-list").append(
                '<tr style="text-align:center" class="project-status" id="'+data.file_list[j].file+'">'+
                    '<td style="white-space: nowrap; overflow:hidden;text-overflow: ellipsis; width: 30vw; background-color: '+color+';">'+data.file_list[j].file+'</td>'+
                    '<td style="background-color: '+color+'">'+result_eval+'</td>'+
                    '<td style="background-color: '+color+';">'+data.file_list[j].state+'</td>'+
                '</tr>'
            );
        }

        $(".project-status").click(function (e) {
            let file = $(this).attr("id");
            

            eel.get_image(file)(function (data) {
                $("#before").attr('src', 'data:image/png;base64,'+data.before);
                $("#after").attr('src', 'data:image/png;base64,'+data.after);
                selected_image = file;
                
            });
            $(".modal-img").show();
        });
    }
    else{
        alert("Error while refreshing");
    }
}


$(document).ready(function () {
    $("#btn-start-prediction").click(function (e) {
        eel.start_prediction()(function (data) {
            $("#btn-stop-prediction").show();
            $("#btn-start-prediction").hide();
        });
    });

    $("#btn-stop-prediction").click(function (e) {

        eel.stop_prediction()( (data) => {
            $("#btn-stop-prediction").hide();
            $("#btn-start-prediction").show();
        });
        

    });

    $("#btn-refresh-project").click(function (e) {
        alert("refresh");
        eel.get_updated_model()(update_image_list);
    });

    $("#btn-sort-certain").click(function (e) {
        models[selected_model].file_list.sort(function (a, b) {
            if(a.evaluation <= -1) return 1;
            return Math.abs(b.evaluation) - Math.abs(a.evaluation);
        });
        update_image_list(models[selected_model]);
    });

    
    $("#btn-sort-doubt").click(function (e) {
        models[selected_model].file_list.sort(function (a, b) {
            return Math.abs(a.evaluation) - Math.abs(b.evaluation);
        });
        update_image_list(models[selected_model]);
    });
    

});