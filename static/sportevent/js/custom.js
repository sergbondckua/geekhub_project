(function ($) {

    "use strict";

    // MENU
    $('.navbar-collapse a').on('click', function () {
        $(".navbar-collapse").collapse('hide');
    });

    // CUSTOM LINK
    $('.smoothscroll').click(function () {
        var el = $(this).attr('href');
        var elWrapped = $(el);
        var header_height = $('.navbar').height();

        scrollToDiv(elWrapped, header_height);
        return false;

        function scrollToDiv(element, navheight) {
            var offset = element.offset();
            var offsetTop = offset.top;
            var totalScroll = offsetTop - 0;

            $('body,html').animate({
                scrollTop: totalScroll
            }, 300);
        }
    });

    // $('.owl-carousel').owlCarousel({
    //     center: true,
    //     loop: true,
    //     margin: 30,
    //     autoplay: true,
    //     responsiveClass: true,
    //     responsive: {
    //         0: {
    //             items: 2,
    //         },
    //         767: {
    //             items: 3,
    //         },
    //         1200: {
    //             items: 4,
    //         }
    //     }
    // });

})(window.jQuery);

$(document).ready(function () {
    $('button[data-bs-toggle="tab"]').on('shown.bs.tab', function () {
        $.fn.dataTable.tables({visible: true, api: true}).columns.adjust();
    });
    $('table.tbl').DataTable(
        {
            dom: 'frti',
            order: [[7, 'asc']],
            columnDefs: [
                {
                    orderable: false,
                    targets: [1, 2, 3, 4, 5, 6, 7]
                },
                {
                    type: 'time-uni', targets: 7
                },
                {
                    searchable: false,
                    orderable: false,
                    targets: 0,
                },
            ],
            language: {
                url: 'https://cdn.datatables.net/plug-ins/1.11.5/i18n/uk.json',
            },
            lengthMenu: [
                [-1, 10, 15, 40],
                ["♾️", 10, 15, 40],
            ],
            rowCallback: function (row, data, index) {
                let idx = index + 1;
                $('th:eq(0)', row).html(idx);
            },

            initComplete: function () {
                this.api().columns([3]).every(function () {
                    let column = this;
                    let select = $('<select><option value="">Стать</option></select>')
                        .appendTo($(column.header()).empty())
                        .on('change', function () {
                            let val = $.fn.dataTable.util.escapeRegex($(this).val());

                            column.search(val ? '^' + val + '$' : '', true, false).draw();
                        });

                    column
                        .data()
                        .unique()
                        .sort()
                        .each(function (d, j) {
                            let val = $('<div/>').html(d).text();
                            select.append('<option value="' + val + '">' + val + '</option>');
                        });
                });
            },
        }
    );
});