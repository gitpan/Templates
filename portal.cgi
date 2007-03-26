#!/usr/bin/perl

use strict;
use CGI::Portal;

    CGI::Portal::activate({'database_type'       => "mysql",

                           'database_name'       => "some_name",
                           'database_host'       => "localhost",
                           'database_user'       => "some_user",
                           'database_passw'      => "some_password",

                           'user_table'          => "users",
                           'user_index_field'    => "id",
                           'user_user_field'     => "user",
                           'user_passw_field'    => "passw",
                           'user_additional'     => ["email","first_name","middle_initial","last_name","city","state","country"],
                           # at least:              ["email"],

                           'session_table'       => "sessions",
                           'session_index_field' => "id",
                           'session_sid_field'   => "sid",
                           'session_user_field'  => "user",
                           'session_start_field' => "session_start",
                           'session_additional'  => "",


                           # Modules in the CGI::Portal::Scripts namespace, the first is the default action

                           'actions'             => ["logon", "logoff", "register", "profile", "changepw", "emailpw"],

                           'session_length'      => 7200,
                           'admin_email'         => "some_user\@some_host.com",

                           'template_dir'        => "templates/", # include trailing slash
                           'header_html'         => "header.html",
                           'footer_html'         => "footer.html",
                           'logon_success_html'  => "logon.html"});