<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="refresh" content="300" />

        <title>SSI Urgencias</title>

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

        <!-- Styles -->
        <style>
            .full-height {
                height: 95vh;
            }
            .position-ref {
                position: relative;
            }
            .content {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="position-ref full-height">

            <div class="content">

                <h1>Urgencias</h1>

                <table class="table table-sm table-bordered h2">
                    <thead>
                        <tr>
                            <th>Establecimiento</th>
                            <th>Pacientes</th>
                        </tr>
                    </thead>
                    <tbody>
                        @foreach($establishments as $estab)
                        <tr>
                            <td class="p-3">
                                {{ $estab->name }}
                                <br>
                                <!--small>{{ $estab->address }}</small-->
                                <small class="text-muted">Actualizado a las {{ $estab->waitingList->last()->updated_at->format('H:i:s') }}</small>
                            </td>
                            <td class="pt-3">{{ $estab->waitingList->last()->waiting }}</td>
                        </tr>
                        @endforeach
                    </tbody>
                </table>

            </div>

        </div>

        <footer class="footer">
            <div class="col-8 col-md-6 d-inline-block text-white"
                style="background-color: rgb(0,108,183);">Servicio de Salud Iquique</div>
            <div class="col-4 col-md-6 float-right text-white"
                style="background-color: rgb(239,65,68);"> © 2019</div>
        </footer>

    </body>
</html>
