$('.preforms_select').select2({
    language: 'es',
    allowClear: true,
    ajax: {
        delay: 250,
        type: 'POST',
        url: window.location.pathname,
        data: function (params) {
            var queryParameters = {
                term: params.term,
                action: 'searchdata'
              }
          
              return queryParameters;
        },
        processResults: function (data) {
            return {
              results: data
            };
          },
    },
    placeholder: 'Selecciona un Cliente',
    minimumInputLength: 2,
});