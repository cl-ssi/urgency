<?php

use Illuminate\Database\Seeder;
use App\Establishment;

class EstablishmentTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $estab = new Establishment();
        $estab->name = 'SAPU Aguirre';
        $estab->address = 'Chintaguay S/N';
        $estab->save();

        $estab = new Establishment();
        $estab->name = 'SAPU Guzmán';
        $estab->address = 'Pedro Prado';
        $estab->save();

        $estab = new Establishment();
        $estab->name = 'SAPU Videla';
        $estab->address = 'Arturo Fernandez';
        $estab->save();

        $estab = new Establishment();
        $estab->name = 'SAPU Sur';
        $estab->address = 'Playa El Aguila';
        $estab->save();

        $estab = new Establishment();
        $estab->name = 'SAPU El Boro';
        $estab->address = 'Alto Hospicio';
        $estab->save();

        $estab = new Establishment();
        $estab->name = 'SAPU Pedro Pulgar';
        $estab->address = 'Alto Hospicio';
        $estab->save();

        $estab = new Establishment();
        $estab->name = 'Urgencia Reyno';
        $estab->address = 'Alto Hospicio';
        $estab->save();
    }
}
