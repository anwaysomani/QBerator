$(function () {
  $(".js-create-question").click(function () {
    $.ajax({
      url: '/questions/create/',
      type: 'get',
      // dataType: 'json',
      beforeSend: function () {
        $("#modal-question").modal("show");
      },
      success: function (data) {
        $("#modal-question .modal-content").html(data.html_form);
      }
    });
  });
});