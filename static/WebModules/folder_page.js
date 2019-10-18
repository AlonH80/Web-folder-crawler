function request_folder(folder_path){
    $.ajax({
        data: JSON.stringify({"folder_path":folder_path}),
        contentType: 'application/json;charset=UTF-8',
        url: "folder_search",
        method: 'POST',
        success: function(data){
            document.body.innerHTML = "";
            document.write(data);

        },
        error: function (er) {
            console.log(er);
        }
    });
}

function request_file_content(file_path){
    file_cont = "";
    $.ajax({
        data: JSON.stringify({"file_path":file_path}),
        contentType: 'application/json;charset=UTF-8',
        url: "file_content",
        method: 'POST',
        success: function(data){            
            file_cont = data;
        },
        error: function (er) {
            console.log(er);
        }
    });

    return file_cont;   
}


function fill_file_content(content){
    file_cont_node = $("#file_content")[0];
    file_cont_node.textContent = content;
}


function download_file(file_path){
    cont = request_file_content(file_path)
    var blob = new Blob([cont], {type: "text/plain"});
    file_path_splitted = file_path.split("/");
    file_name = file_path_splitted[file_path_splitted.length - 1]
    saveAs(blob, file_name);
}