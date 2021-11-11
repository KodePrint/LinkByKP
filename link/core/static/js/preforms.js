/* OBTIENIENDO LAS VARIABLES A UTILIZAR */
var addDetailBtn = document.querySelector('.add_detail_btn');
var description = document.getElementsByName('description');
var mount = document.getElementsByName('mount');

/* AGREGANDO AL DETALLE AL HACER CLICK EN EL BOTON DE MAS*/
addDetailBtn.addEventListener('click', () => {
    detail = {
        Description: description.values(),
        cost: mount.values(),
    };
    preformItem.add(detail)
})

/* CREAMOS EL DICCIONARIO QUE GUARDARA LA PREFORMA */
var preformItem = {
    /* Creamos un diccionario con los campos */
    items: {
        identifier: "",
        date: "",
        client: "",
        total_cost: 0.0,
        state: "",
        details: []
    },
    // Creamos la funcion para Calcular el totla 
    calculate: "",
    // Creamos la funcion para agregar detalles al diccionario
    add: function(item) {
        list = [];
        this.items.details.push(item);


        // Validamos que sea el primer detalle
        /*if (this.items.details.length == 0) {
            this.items.details.push(item);
        } else { // De lo contrario creamos un listado con los ID de los detalles agregados
            list = [];
            $.each(this.items.details, (index, value) => {
                list.push(value.id);
            });
            Preguntamos si existe el id en la lista temporal
            if (listado.includes(item.id)) {
                alertMsg('Opps..!', 'El Producto ya esta en la lista..!');
            } else {
                Si no existe lo agregamos
                this.items.productos.push(item);
            }
        }*/
        console.log(detail);
        this.list();
    },
}


$('.preforms_select').select2({
    language: 'es',
    allowClear: true,
    ajax: {
        delay: 250,
        type: 'POST',
        url: window.location.pathname,
        data: function(params) {
            var queryParameters = {
                term: params.term,
                action: 'searchdata'
            }

            return queryParameters;
        },
        processResults: function(data) {
            return {
                results: data
            };
        },
    },
    placeholder: 'Selecciona un Cliente',
    minimumInputLength: 2,
});

var clientSelect = document.querySelector('.select2-selection__rendered');

clientSelect.addEventListener('click', () => {
    if (document.querySelector('.select2-search__field') != null) {
        document.querySelector('.select2-search__field').focus();
    };
});