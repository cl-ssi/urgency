<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Establishment extends Model
{
    public function waitingList() {
        return $this->hasMany('App\WaitingList');
    }
}
