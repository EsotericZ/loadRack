const pusher = new Pusher("6fd0f7485811f36fa809", {
    cluster: "us3",
    encrypted: true
});

var channel = pusher.subscribe('table');

channel.bind('new-record', (data) => {
    $('#rows').append('
        <tr id="${data.data.id}">
            <th scope="row"> ${data.data.rack} </th>
            <td> ${data.data.row} </td>
            <td> ${data.data.matl} </td>
            <td> ${data.data.size} </td>
            <td> ${data.data.note} </td>
            <td> ${data.data.weight} </td>
            <td> ${data.data.phidget} </td>
        </tr>
    ')
});

channel.bind('upgrade-record', (data) => {
    $('#{data.data.id}').html('
        <th scope="row"> ${data.data.rack} </th>
        <td> ${data.data.row} </td>
        <td> ${data.data.matl} </td>
        <td> ${data.data.size} </td>
        <td> ${data.data.note} </td>
        <td> ${data.data.weight} </td>
        <td> ${data.data.phidget} </td>
    ')
});

// TOGGLE NAVBAR
$(document).ready(function () {
            $('#sidebarCollapse').on('click', function () {
                $('#sidebar').toggleClass('active');
            });
        });
