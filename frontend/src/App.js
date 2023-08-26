import React, { useState } from 'react';

function App() {
    const [imageInput, setImageInput] = useState(null);
    const [result, setResult] = useState('');
    const [displayedImage, setDisplayedImage] = useState(null);

    const handleSubmit = () => {
        if (!imageInput) return;

        const formData = new FormData();
        formData.append('image', imageInput);

        fetch('http://127.0.0.1:5000/classify', {
                method: 'POST',
                body: formData,
            })
            .then((response) => response.json())
            .then((result) => {
                const classification = result.classification;
                const probability = result.probability.toFixed(2);
                setResult(
                    `Result: ${classification}\nAccuracy: ${probability}%`
                );
                setDisplayedImage(URL.createObjectURL(imageInput));
            });
    };

    return ( <
        div className = "App" >
        <
        h1 > Skin Cancer Classification < /h1> <
        input type = "file"
        onChange = {
            (event) => setImageInput(event.target.files[0]) }
        /> <
        button onClick = { handleSubmit } > Submit < /button> <
        p > { result } < /p> { displayedImage && < img src = { displayedImage }
            alt = "Uploaded skin image" / > } <
        /div>
    );
}

export default App;