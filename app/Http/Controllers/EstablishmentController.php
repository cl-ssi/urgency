<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Establishment;

class EstablishmentController extends Controller
{
    public function index()
    {
        $establishments = Establishment::all();
        return view('index', compact('establishments'));
    }
}
