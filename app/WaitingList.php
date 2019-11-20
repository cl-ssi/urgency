<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class WaitingList extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'waiting', 'establishment_id'
    ];

    public function establishment() {
        return $this->belongsTo('App\Establishment');
    }
}
