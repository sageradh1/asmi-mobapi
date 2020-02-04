--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: asmi_group
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO asmi_group;

--
-- Name: api_auth_key; Type: TABLE; Schema: public; Owner: asmi_group
--

CREATE TABLE public.api_auth_key (
    id integer NOT NULL,
    api_key character varying(100),
    generate_date timestamp without time zone,
    expiry_date timestamp without time zone
);


ALTER TABLE public.api_auth_key OWNER TO asmi_group;

--
-- Name: api_auth_key_id_seq; Type: SEQUENCE; Schema: public; Owner: asmi_group
--

CREATE SEQUENCE public.api_auth_key_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_auth_key_id_seq OWNER TO asmi_group;

--
-- Name: api_auth_key_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asmi_group
--

ALTER SEQUENCE public.api_auth_key_id_seq OWNED BY public.api_auth_key.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: asmi_group
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    first_name character varying(64),
    last_name character varying(64),
    username character varying(64),
    email character varying(120),
    _phone_number character varying(255),
    phone_country_code character varying(8),
    date_of_birth timestamp without time zone NOT NULL,
    password_hash character varying(128),
    created_datetime timestamp without time zone,
    gender character varying(64),
    is_active boolean,
    lastonline_time timestamp without time zone
);


ALTER TABLE public."user" OWNER TO asmi_group;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: asmi_group
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO asmi_group;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asmi_group
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: video_post; Type: TABLE; Schema: public; Owner: asmi_group
--

CREATE TABLE public.video_post (
    id integer NOT NULL,
    filename character varying(100),
    extension character varying(5),
    storagelocation character varying(500),
    upload_started_time timestamp without time zone,
    upload_completed_time timestamp without time zone,
    last_modified_time timestamp without time zone,
    caption character varying(440),
    user_id integer,
    audio_info character varying(200)
);


ALTER TABLE public.video_post OWNER TO asmi_group;

--
-- Name: video_post_id_seq; Type: SEQUENCE; Schema: public; Owner: asmi_group
--

CREATE SEQUENCE public.video_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.video_post_id_seq OWNER TO asmi_group;

--
-- Name: video_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asmi_group
--

ALTER SEQUENCE public.video_post_id_seq OWNED BY public.video_post.id;


--
-- Name: api_auth_key id; Type: DEFAULT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public.api_auth_key ALTER COLUMN id SET DEFAULT nextval('public.api_auth_key_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: video_post id; Type: DEFAULT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public.video_post ALTER COLUMN id SET DEFAULT nextval('public.video_post_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: asmi_group
--

COPY public.alembic_version (version_num) FROM stdin;
6ddc44899203
\.


--
-- Data for Name: api_auth_key; Type: TABLE DATA; Schema: public; Owner: asmi_group
--

COPY public.api_auth_key (id, api_key, generate_date, expiry_date) FROM stdin;
1	ab56ba0ae9d7413dacd395e378e8f1f3	2020-02-02 09:30:01.304156	2030-01-30 09:30:01.304156
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: asmi_group
--

COPY public."user" (id, first_name, last_name, username, email, _phone_number, phone_country_code, date_of_birth, password_hash, created_datetime, gender, is_active, lastonline_time) FROM stdin;
\.


--
-- Data for Name: video_post; Type: TABLE DATA; Schema: public; Owner: asmi_group
--

COPY public.video_post (id, filename, extension, storagelocation, upload_started_time, upload_completed_time, last_modified_time, caption, user_id, audio_info) FROM stdin;
\.


--
-- Name: api_auth_key_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asmi_group
--

SELECT pg_catalog.setval('public.api_auth_key_id_seq', 1, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asmi_group
--

SELECT pg_catalog.setval('public.user_id_seq', 1, false);


--
-- Name: video_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asmi_group
--

SELECT pg_catalog.setval('public.video_post_id_seq', 1, false);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: api_auth_key api_auth_key_pkey; Type: CONSTRAINT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public.api_auth_key
    ADD CONSTRAINT api_auth_key_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: video_post video_post_filename_key; Type: CONSTRAINT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public.video_post
    ADD CONSTRAINT video_post_filename_key UNIQUE (filename);


--
-- Name: video_post video_post_pkey; Type: CONSTRAINT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public.video_post
    ADD CONSTRAINT video_post_pkey PRIMARY KEY (id);


--
-- Name: ix_api_auth_key_expiry_date; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_api_auth_key_expiry_date ON public.api_auth_key USING btree (expiry_date);


--
-- Name: ix_api_auth_key_generate_date; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_api_auth_key_generate_date ON public.api_auth_key USING btree (generate_date);


--
-- Name: ix_user_created_datetime; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_user_created_datetime ON public."user" USING btree (created_datetime);


--
-- Name: ix_user_date_of_birth; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_user_date_of_birth ON public."user" USING btree (date_of_birth);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: ix_user_gender; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_user_gender ON public."user" USING btree (gender);


--
-- Name: ix_user_lastonline_time; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_user_lastonline_time ON public."user" USING btree (lastonline_time);


--
-- Name: ix_user_username; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE UNIQUE INDEX ix_user_username ON public."user" USING btree (username);


--
-- Name: ix_video_post_last_modified_time; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_video_post_last_modified_time ON public.video_post USING btree (last_modified_time);


--
-- Name: ix_video_post_upload_completed_time; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_video_post_upload_completed_time ON public.video_post USING btree (upload_completed_time);


--
-- Name: ix_video_post_upload_started_time; Type: INDEX; Schema: public; Owner: asmi_group
--

CREATE INDEX ix_video_post_upload_started_time ON public.video_post USING btree (upload_started_time);


--
-- Name: video_post video_post_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asmi_group
--

ALTER TABLE ONLY public.video_post
    ADD CONSTRAINT video_post_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- PostgreSQL database dump complete
--

