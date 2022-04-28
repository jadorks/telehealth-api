const container = document.getElementById("video-container");

document.addEventListener('DOMContentLoaded', async function(){
    const room = await joinVideoRoom();

    handleConnectedParticipant(room.localParticipant);
    room.participants.forEach(handleConnectedParticipant);
    room.on("participantConnected", handleConnectedParticipant);

    room.on("participantDisconnected", handleDisconnectedParticipant);
    window.addEventListener("pagehide", () => room.disconnect());
    window.addEventListener("beforeunload", () => room.disconnect());
}, false)

const handleConnectedParticipant = (participant) => {
    const participantDiv = document.createElement("div");
    participantDiv.setAttribute("id", participant.identity);
    container.append(participantDiv);

    participant.tracks.forEach((trackPublication) => {
        handleTrackPublication(trackPublication, participant);
    });

    participant.on("trackPublished", handleTrackPublication)
};

const handleTrackPublication = (trackPublication, participant) => {
    function displayTrack(track) {

    const participantDiv = document.getElementById(participant.identity);

      participantDiv.append(track.attach());
    }

    if (trackPublication.track) {
      displayTrack(trackPublication.track);
    }

    trackPublication.on("subscribed", displayTrack);
  };
  

const handleDisconnectedParticipant = (participant) => {
    participant.removeAllListeners();
    const participantDiv = document.getElementById(participant.identity);
    participantDiv.remove()
}

const joinVideoRoom = async () => {
  const room = await Twilio.Video.connect(context.participant_token, {
    room: context.room_name,
  });
  return room;
};