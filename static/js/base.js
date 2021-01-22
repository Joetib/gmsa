function readURL(input, destination) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            destination.innerText = "";
            let img = document.createElement("img");
            img.src = e.target.result;
            img.classList.add("img-default");
            img.style.height = "100%";
            destination.appendChild(img);
        }

        reader.readAsDataURL(input.files[0]); // convert to base64 string
    }
}

function readMultipleURL(input, destination) {
    if (input.files && input.files[0]) {

        destination.innerText = "";
        for (item of input.files){
            var reader = new FileReader();

            reader.onload = function (e) {
                let column = document.createElement("div");
                column.classList.add("col-6");
                column.classList.add("col-sm-4");
                column.classList.add("col-md-4");
                column.classList.add("p-0");

                let img = document.createElement("img");
                img.src = e.target.result;
                img.classList.add("img-thumbnail");
                img.style.height="100px"
                img.style.width = "100px";
                img.style.objectFit = "cover";
                destination.appendChild(img);
                column.appendChild(img);
                destination.appendChild(column);
            }

            reader.readAsDataURL(item);
        };
        //reader.readAsDataURL(input.files[0]); // convert to base64 string
    }
}


$(document).ready(function () {
    let items = document.getElementsByClassName("image-form-section")
    for (let item  of items ) {
        item.querySelector("input[type='file']").addEventListener("change", (e) => {
            readMultipleURL(e.target, item.querySelector(".img-display"))
        });
    }
});
