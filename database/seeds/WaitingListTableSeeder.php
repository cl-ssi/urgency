<?php

use Illuminate\Database\Seeder;
use App\WaitingList;

class WaitingListTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $w = new WaitingList();
        $w->waiting = 0;
        $w->establishment_id = 1;
        $w->save();

        $w = new WaitingList();
        $w->waiting = 0;
        $w->establishment_id = 2;
        $w->save();

        $w = new WaitingList();
        $w->waiting = 0;
        $w->establishment_id = 3;
        $w->save();

        $w = new WaitingList();
        $w->waiting = 0;
        $w->establishment_id = 4;
        $w->save();

        $w = new WaitingList();
        $w->waiting = 0;
        $w->establishment_id = 5;
        $w->save();

        $w = new WaitingList();
        $w->waiting = 0;
        $w->establishment_id = 6;
        $w->save();

        $w = new WaitingList();
        $w->waiting = 0;
        $w->establishment_id = 7;
        $w->save();
    }
}
