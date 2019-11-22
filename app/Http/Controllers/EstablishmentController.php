<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Establishment;

class EstablishmentController extends Controller
{
    public function movil()
    {
        $establishments = Establishment::all();
        return view('movil', compact('establishments'));
    }

    public function tv()
    {
        $establishments = Establishment::all();
        return view('tv', compact('establishments'));
    }
}
