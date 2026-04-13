// document.getElementById('imageUpload').addEventListener('change', function(event) {
//             const file = event.target.files[0]; // Get the selected file
            
//             if (file) {
//                 // Create a temporary URL for the image
//                 const imageUrl = URL.createObjectURL(file);
                
//                 // Display the image
//                 const preview = document.getElementById('previewImage');
//                 preview.src = imageUrl;
//                 preview.style.display = 'block'; // Make the image visible
//             }
//         })

passwordControl = document.getElementById("pwd");
passwordControl.addEventListener('change',test)
function test(event)
{
    //alert('hi');
    alert(event.target.value);

}