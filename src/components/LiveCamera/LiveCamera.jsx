import "./LiveCamera.css";

function LiveCamera() {

    return (

        <div className="camera-container">

            <h2>Live AI Camera</h2>

            <img

                src="http://127.0.0.1:5000/video_feed"

                alt="Live Camera"

                width="100%"

            />

        </div>

    );

}

export default LiveCamera;