$(document).ready(function(){
    var csrfToken = "{{ csrf_token }}";
    var table = $("#iha_list").DataTable({
        responsive: true,
        processing: true,
        pageLength: 10,
        serverSide: true,
        ajax: {
            url: "/iha-list-search/",
            type: "GET",
            beforeSend: function(xhr){
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        },
        columnDefs: [
            {"targets":0, "title":"İha İsimi"},
            {"targets":1, "title":"İha Modeli"},
            {"targets":2, "title":"Saatlik Fiyatı"},
            {"targets":3, "title":"Mevcut"},
            {"targets":4, "title":"İşlem"},

        ],
        columns: [
            {data : 'isim'},
            {data : 'model'},
            {data : 'saatlik_fiyat'},
            {data : 'mevcut'},
            {data : 'id',
                render: function(data ,type, row, meta){
                    return '<a href="javascript:void(0)" class="delete-link" data-id="' + data +'">Sil</a>'
                }
            },
            
        ]
    });

    $('#iha_list').on('click', '.delete-link', function(e) {
        e.preventDefault();
        var id = $(this).data('id');
        
        if (confirm("Bu İHA'yı silmek istediğinize emin misiniz?")) {
            $.ajax({
                url: '/iha/' + id + '/delete/',
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: $('meta[name="csrf-token"]').attr('content')
                },
                success: function(response) {
                    $("#success_delete").show();
                    setTimeout(function() { 
                        $("#success_delete").hide();
                    }, 2000);
                    table.ajax.reload();
                },
                error: function(xhr, status, error) {
                    console.error("Silme işlemi sırasında bir hata oluştu.");
                }
            });
        }
    });
})

$(document).ready(function(){
    var csrfToken = "{{ csrf_token }}";
    var table = $("#customerTable").DataTable({
        responsive: true,
        processing: true,
        pageLength: 10,
        serverSide: true,
        ajax: {
            url: "/customer-list-search/", 
            type: "GET",
            beforeSend: function(xhr){
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        },
        columnDefs: [
            {"targets": 0, "title": "First Name", "data": "first_name"},
            {"targets": 1, "title": "Last Name", "data": "last_name"},
            {"targets": 2, "title": "Email", "data": "email"},
            {"targets": 3, "title": "Phone Number", "data": "phone_number"},
            {"targets": 4, "title": "Actions", 
                "render": function(data, type, row, meta) {
                    return '<a href="javascript:void(0)" class="delete-link" data-id="' + row.id + '">Delete</a>';
                }
            }
        ],
        columns: [
            {data: 'first_name'},
            {data: 'last_name'},
            {data: 'email'},
            {data: 'phone_number'},
            {data: null,
                render: function(data, type, row, meta){
                    return '<a href="javascript:void(0)" class="delete-link" data-id="' + row.id +'">Delete</a>';
                }
            }
        ]
    });

    $('#customerTable').on('click', '.delete-link', function(e) {
        e.preventDefault();
        var id = $(this).data('id');
        
        if (confirm("Are you sure you want to delete this customer?")) {
            $.ajax({
                url: '/customer/' + id + '/delete/',  
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: csrfToken
                },
                success: function(response) {
                    $("#success_delete").show();
                    setTimeout(function() { 
                        $("#success_delete").hide();
                    }, 2000);
                    table.ajax.reload();
                },
                error: function(xhr, status, error) {
                    console.error("An error occurred while deleting.");
                }
            });
        }
    });
});
